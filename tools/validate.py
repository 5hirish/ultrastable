#!/usr/bin/env python3
"""Validate Ultrastable spec examples and experiment records.

Usage:
    python tools/validate.py            # validate everything
    python tools/validate.py PATH ...   # validate specific files

Checks:
  * spec/examples/jobs*.yaml          against spec/jobs.schema.json
  * spec/examples/policy*.yaml        against spec/policy.schema.json, plus level <= cap
  * spec/examples/ledger/*.yaml       against spec/ledger.schema.json, plus id/file name
                                      match and state-dependent required fields
  * experiments/NN-*.md front matter  required keys, allowed statuses, decision rules
  * Markdown files                    no em dashes (project style rule)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
LEVELS = ["A0", "A1", "A2", "A3"]
EXPERIMENT_KEYS = {"id", "title", "status", "weeks", "hypothesis", "metric", "kill_signal", "decision"}
STATUSES = {"planned", "running", "done", "killed"}
DECISIONS = {None, "continue", "adjust", "kill"}


def load_schema(name: str) -> Draft202012Validator:
    schema = json.loads((ROOT / "spec" / name).read_text())
    return Draft202012Validator(schema, format_checker=FormatChecker())


def yaml_load(path: Path):
    # Dates must stay strings so they match the schema's string type.
    class Loader(yaml.SafeLoader):
        pass

    Loader.yaml_implicit_resolvers = {
        k: [r for r in v if r[0] != "tag:yaml.org,2002:timestamp"]
        for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
    }
    return yaml.load(path.read_text(), Loader=Loader)


def schema_errors(validator: Draft202012Validator, data) -> list[str]:
    return [
        f"{'/'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}"
        for e in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
    ]


def check_jobs(path: Path) -> list[str]:
    data = yaml_load(path)
    errors = schema_errors(load_schema("jobs.schema.json"), data)
    ids = [j.get("id") for j in (data or {}).get("jobs", [])]
    if len(ids) != len(set(ids)):
        errors.append("jobs: duplicate job ids")
    return errors


def check_policy(path: Path) -> list[str]:
    data = yaml_load(path)
    errors = schema_errors(load_schema("policy.schema.json"), data)
    for name, cls in (data or {}).get("classes", {}).items():
        if isinstance(cls, dict) and cls.get("level") in LEVELS and cls.get("cap") in LEVELS:
            if LEVELS.index(cls["level"]) > LEVELS.index(cls["cap"]):
                errors.append(f"classes/{name}: level {cls['level']} is above cap {cls['cap']}")
    return errors


def check_ledger(path: Path) -> list[str]:
    data = yaml_load(path)
    errors = schema_errors(load_schema("ledger.schema.json"), data)
    if not isinstance(data, dict):
        return errors
    if data.get("id") and data["id"] != path.stem:
        errors.append(f"id {data['id']} does not match file name {path.stem}")
    state = data.get("state")
    if state in {"shipped", "measured", "rolled_back"} and "shipped" not in data:
        errors.append(f"state {state} requires a 'shipped' block")
    if state == "measured" and "measured" not in data:
        errors.append("state measured requires a 'measured' block")
    if state in {"verified", "shipped", "measured"} and "verification" not in data:
        errors.append(f"state {state} requires a 'verification' block")
    return errors


def check_experiment(path: Path) -> list[str]:
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return ["missing YAML front matter"]
    meta = yaml.safe_load(match.group(1)) or {}
    errors = [f"missing key: {k}" for k in sorted(EXPERIMENT_KEYS - meta.keys())]
    if meta.get("status") not in STATUSES:
        errors.append(f"status must be one of {sorted(STATUSES)}")
    if meta.get("decision") not in DECISIONS:
        errors.append("decision must be continue, adjust, kill or null")
    if meta.get("status") in {"done", "killed"} and not meta.get("decision"):
        errors.append(f"status {meta.get('status')} requires a decision")
    for key in ("hypothesis", "metric", "kill_signal"):
        if key in meta and not str(meta[key] or "").strip():
            errors.append(f"{key} must not be empty")
    if not path.stem.startswith(str(meta.get("id", ""))):
        errors.append("file name must start with the experiment id")
    return errors


def check_style(path: Path) -> list[str]:
    errors = []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if "\u2014" in line:
            errors.append(f"line {n}: em dash found, rewrite the sentence")
    return errors


def checks_for(path: Path):
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("spec/examples/ledger/") and path.suffix in {".yaml", ".yml"}:
        yield check_ledger
    elif rel.startswith("spec/examples/jobs") and path.suffix in {".yaml", ".yml"}:
        yield check_jobs
    elif rel.startswith("spec/examples/policy") and path.suffix in {".yaml", ".yml"}:
        yield check_policy
    if rel.startswith("experiments/") and re.match(r"^\d{2}-", path.name):
        yield check_experiment
    if path.suffix == ".md":
        yield check_style


def all_targets() -> list[Path]:
    files = list((ROOT / "spec" / "examples").rglob("*.y*ml"))
    files += [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    return sorted(files)


def main(argv: list[str]) -> int:
    targets = []
    for arg in argv:
        p = Path(arg).resolve()
        targets += sorted(x for x in p.rglob("*") if x.is_file()) if p.is_dir() else [p]
    targets = targets or all_targets()

    failed = 0
    checked = 0
    for path in targets:
        for check in checks_for(path):
            checked += 1
            errors = check(path)
            if errors:
                failed += 1
                print(f"FAIL {path.relative_to(ROOT)} ({check.__name__})")
                for e in errors:
                    print(f"  - {e}")
    print(f"\n{checked} checks, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
