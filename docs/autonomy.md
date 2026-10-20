# Autonomy model

Autonomy is granted per **change class**, never globally, and it is earned with a track
record. The levels are defined in [`CHARTER.md`](../CHARTER.md#4-autonomy-levels).

## Change classes (v0.1)

| Class | Loop | Examples | Starting level | Cap in v0.1 |
| --- | --- | --- | --- | --- |
| `copy` | L1 / L3 | Labels, help text, empty states | A1 | A3 |
| `layout-adapt` | L1 | Component order, defaults, shortcuts in declared slots | A1 | A2 |
| `bugfix-frontend` | L2 | Dead clicks, broken handlers, render errors | A1 | A3 |
| `bugfix-backend` | L2 | Exceptions with a reproduction test | A1 | A2 |
| `performance` | L2 | Query, bundle and render optimizations | A1 | A2 |
| `dependency-security` | L2 | Patch and minor upgrades fixing known CVEs | A1 | A2 |
| `feature` | L3 | New flows or capabilities | A0 | A1 |
| `schema` | L3 | Database or API schema | A0 | A1 |
| `infra` | L3 | Scaling, regions, services | A0 | A1 |
| `auth-payments-deletion` | any | Anything touching login, money or data removal | A0 | A1 |

## Promotion and demotion

- **Promote** one level after 20 consecutive changes in that class with no rollback, no human
  rewrite and no guardrail breach. Promotion is a pull request to the policy file, approved
  by a human.
- **Demote** to A1 immediately on any incident, rollback caused by a real-user guardrail
  breach, or a red-team finding in that class.
- The ledger is the evidence for both. Promotion without ledger evidence is not allowed.

## The policy file

The owner keeps a policy file in their repo. See
[`spec/examples/policy.yaml`](../spec/examples/policy.yaml) and its schema
[`spec/policy.schema.json`](../spec/policy.schema.json).
