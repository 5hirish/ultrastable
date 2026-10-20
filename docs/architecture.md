# Architecture (draft v0.1)

This is a target architecture, not built code. Each part is built only when an experiment in
[`ROADMAP.md`](../ROADMAP.md) needs it.

## The loop as MAPE-K

```
           +-------------------- Knowledge ---------------------+
           |  jobs manifest . evolution ledger . autonomy policy |
           +------------------------------------------------------+
                ^            ^             ^              ^
   signals      |            |             |              |
 ---------> [ Monitor ] -> [ Analyze ] -> [ Plan ] -> [ Execute ]
  (senses)    collect,      diagnose,     propose       verify, then
              filter        hypothesize   candidates    deploy by policy
```

| MAPE-K phase | Ultrastable component | Trust boundary |
| --- | --- | --- |
| Monitor | **Senses**: signal adapters plus an injection filter | Reads untrusted data, no write access |
| Analyze | **Diagnostician**: clusters signals, scores jobs, writes hypotheses to the ledger | Reads filtered data, writes only to the ledger |
| Plan | **Mutator**: a pluggable coding agent producing candidate changes | Sandbox, synthetic data, no network |
| Execute (verify) | **Selector and verifier**: replay tests, synthetic users, policy checks | Different model or deterministic code |
| Execute (ship) | **Deployer**: flags, canaries, rollback, merges allowed by policy | No language model inside |
| Knowledge | **Ledger, manifest, policy** | Append-only ledger; manifest and policy edited by humans |

## Separation of powers and the lethal trifecta

| Component | Private data | Untrusted content | External comms / deploy |
| --- | --- | --- | --- |
| Senses | yes | yes | **no** |
| Diagnostician | aggregated only | filtered | **no** |
| Mutator | **no** (synthetic) | hypothesis text only | **no** (sandboxed) |
| Selector | **no** | **no** | **no** |
| Deployer | **no** | **no** | yes, policy only |

No row has all three. Any design change that would put three "yes" values in one row needs
an ADR and a red-team run.

## Change lifecycle

1. A signal arrives (error cluster, rage-click cluster, failing job metric, CVE, survey theme).
2. The diagnostician links it to a job in the manifest and writes a ledger entry in state
   `hypothesis`, with predicted impact.
3. The policy decides the autonomy level for that change class.
4. The mutator produces one or more candidates in a sandbox.
5. The verifier runs: unit tests, replay-derived tests, synthetic users, invariant checks.
   The entry moves to `verified` or `rejected`.
6. The deployer ships behind a flag at the allowed level (A1 opens a PR, A2 canaries).
7. After the measurement window, measured impact is written to the ledger. Guardrail breach
   triggers rollback and state `rolled_back`.

## L1 adaptation path

- The app declares a component catalog (A2UI) and the slots where adaptation is allowed.
- A per-user or per-segment profile selects composition and defaults for allowed slots.
- Changes apply at session start, never mid-task.
- Each adaptation has a one-line explanation and a reset control.
- High-impact adaptations are offered as proposals the user accepts, not imposed.

## Interfaces kept deliberately narrow

| Interface | Shape |
| --- | --- |
| Signal adapter | Emits OpenTelemetry-shaped events with `job`, `source`, `severity`, `evidence_ref` |
| Agent backend | `propose(hypothesis, repo_snapshot, constraints) -> candidate patch + rationale` |
| Verifier | `verify(candidate) -> report{tests, replay_pass_rate, synthetic_job_delta, invariant_violations}` |
| Deployer | `ship(candidate, level) -> flag_key`, `rollback(flag_key)` |

Swapping PostHog for another analytics tool, or Claude Code for OpenHands, should only touch
one adapter.
