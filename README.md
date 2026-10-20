# Ultrastable

**Open-source R&D toward software that observes how it is used, then adapts, heals and evolves itself, safely and with evidence.**

Ultrastable is an experimental framework. You add it to an app, declare what the app is for,
and it runs feedback loops over open-source signals (usage, satisfaction, errors, performance,
security) to propose and ship improvements. Every change carries a hypothesis, a predicted
impact and a measured impact. Nothing reaches users without passing a verifier and an
autonomy policy that the owner controls.

> Status: **R&D, step 0**. No framework code yet. We are building the evidence base one small
> experiment at a time. See [`ROADMAP.md`](ROADMAP.md).

## Why the name

In 1948 W. Ross Ashby built the Homeostat, one of the first machines that adapted itself.
He called its behavior *ultrastability*: a system with two feedback loops. The first loop
keeps it working under normal disturbance. The second loop only fires when an **essential
variable** leaves its safe range, and it changes the system's own structure until the
variable is safe again. That is the design of this project: ordinary adaptation in the inner
loop, structural self-modification in the outer loop, and both bounded by essential
variables the owner declares.

## The three loops

| Loop | What changes | Evidence quality | Cadence | Autonomy today |
| --- | --- | --- | --- | --- |
| **L1 Adapt** | Per-user or per-segment UI composition and defaults, over a component catalog | Medium | Per session | Auto, reversible, user can reset |
| **L2 Heal** | Bugs, performance, crashes, vulnerable dependencies | High | Hours to days | Auto PR, auto-merge for proven low-risk classes |
| **L3 Evolve** | Features, flows, schema, infra | Low to medium | Weeks | Agent proposes, a human decides |

Autonomy is earned per change class, not granted. See [`docs/autonomy.md`](docs/autonomy.md).

## Core primitives

| Primitive | What it is | Spec |
| --- | --- | --- |
| Jobs manifest | The app's jobs-to-be-done, success criteria and guardrails. The fitness function. | [`spec/jobs.schema.json`](spec/jobs.schema.json) |
| Evolution ledger | Append-only record of every change: hypothesis, evidence, prediction, result | [`spec/ledger.schema.json`](spec/ledger.schema.json) |
| Autonomy policy | Which change classes may ship at which autonomy level | [`spec/policy.schema.json`](spec/policy.schema.json) |
| Verifier | Replay tests, synthetic users, canaries and rollback | [`docs/architecture.md`](docs/architecture.md) |

## Repository layout

| Path | What it holds |
| --- | --- |
| [`CHARTER.md`](CHARTER.md) | Mission, principles, safety constitution, licensing, governance |
| [`ROADMAP.md`](ROADMAP.md) | The experiment ladder, gates and kill criteria |
| [`docs/`](docs/) | Vision, research landscape, architecture, autonomy model, glossary, decisions |
| [`experiments/`](experiments/) | One file per experiment: hypothesis, method, metric, result, decision |
| [`spec/`](spec/) | JSON Schemas and worked examples for the core primitives |
| [`tools/validate.py`](tools/validate.py) | Validates every spec example and experiment record |

## Principles in one breath

Open signals only. Protocol first (OpenTelemetry, OpenFeature, A2UI). No change without a
measured hypothesis. No agent holds all three legs of the lethal trifecta. Users can see and
undo every adaptation. Publish what fails, not only what works.

## Contributing

We need product people, HCI researchers, security reviewers and engineers who like
falsifiable experiments. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first.

## Licenses

- Code and tooling: [MIT](LICENSE)
- Documentation, research notes and experiment write-ups: [CC BY 4.0](LICENSE-CONTENT.md)
