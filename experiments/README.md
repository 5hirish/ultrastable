# Experiments

One file per experiment. Each starts with front matter that `tools/validate.py` checks:
`id`, `title`, `status`, `weeks`, `hypothesis`, `metric`, `kill_signal`, `decision`.

Rules:

- Fill in hypothesis, metric and kill signal **before** starting. Do not edit them after.
- Write results whether the experiment worked or not.
- A `done` or `killed` experiment must have a `decision`.
- List AI models used in the Results section.

Copy [`TEMPLATE.md`](TEMPLATE.md) to start a new one. The order lives in
[`../ROADMAP.md`](../ROADMAP.md).
