# Ultrastable Charter v0.1

Ultrastable is an open-source research project. Its goal is software that adapts to the people
using it and keeps improving itself, without losing the owner's control or the user's trust.

Changes to this charter are proposed as pull requests and stay open for 7 days of comment
before a maintainer merges them.

## 1. Mission and scope

**Mission:** close the loop between how software is used and how it changes, with evidence
at every step.

**In scope:**

- A jobs manifest format that tells the system what the app is for and what must never break
- Signal ingestion from open-source tools (product analytics, errors, replays, surveys,
  performance, dependency and code scanning)
- Diagnosis, hypothesis and change proposals for UI, code, performance and security
- Verification before release: replay tests, synthetic users, sandboxes, canaries, rollback
- Per-user and per-segment UI adaptation over a declared component catalog
- An append-only ledger of every change and its measured effect
- A JavaScript and TypeScript reference implementation first

**Out of scope (for now):**

- Building our own coding agent. We orchestrate existing ones (Claude Code, OpenHands, Aider
  and others) through a narrow interface.
- Building our own analytics or error tracker. We read from existing open tools.
- Autonomous changes to authentication, payments, data deletion or database schema. These
  stay human-approved until the project has a published track record (see section 4).
- Optimizing engagement for its own sake. Fitness is job completion, not time spent.

## 2. Research principles

1. **Falsifiable steps.** Every experiment states a hypothesis, one metric, a kill signal and
   a decision before it starts. Results are published whether they succeed or fail.
2. **Small and reusable.** Each step takes one to two weeks and leaves something reusable
   behind: a spec, a tool or a dataset.
3. **Beat a baseline.** Every claim is compared with a baseline, by default PostHog
   Self-driving on the same app. "It works" is not a result; "it beat X on Y" is.
4. **Updating is not benefit.** A change that the system made is not evidence that the
   system improved. Only measured impact on declared jobs counts.
5. **Open signals.** Every signal source and tool in the default stack must be open source
   under an OSI license. Source-available tools may be supported as adapters, never required.
6. **Protocol first.** Prefer OpenTelemetry for signals, OpenFeature for rollout and A2UI for
   generated UI. Platform support comes from protocols, not from many hand-written SDKs.

## 3. Safety constitution

A self-modifying app reads untrusted content (user feedback, replays, error messages), holds
private data and can deploy. That is the lethal trifecta by default. These rules exist to
break it architecturally, not with prompts.

1. **Separation of powers.** No single component may read untrusted signals, hold write
   access to production, and communicate externally.
   - **Senses** read signals. They have no write access.
   - **The mutator** writes code in a sandbox with synthetic data and no network.
   - **The selector** judges candidates against the jobs manifest and the verifier. It runs a
     different model or deterministic code.
   - **The deployer** is policy code with no language model in it. It only moves flags and
     merges what the policy allows.
2. **Signals are data, never instructions.** Text from users, logs or replays is quoted into
   prompts as data and passed through an injection filter before any agent sees it.
3. **Invariants are untouchable.** Anything marked as an invariant in the jobs manifest
   (privacy, accessibility, pricing rules, legal copy) cannot be changed by any loop.
4. **Every change is reversible.** Ship behind a flag, keep the previous version, roll back
   automatically when a guardrail metric breaks.
5. **Users can see and undo.** Every L1 adaptation is explainable in one sentence and
   reversible by the user in one action.
6. **Real user data stays where it is.** Sandboxes run on synthetic or anonymized data.
   Session replays used for tests are scrubbed of personal data first.
7. **Red-team before autonomy.** No change class gains auto-merge until it survives the
   injection test suite in [`experiments/05-immune-system.md`](experiments/05-immune-system.md).

## 4. Autonomy levels

| Level | Name | The system may | Who decides |
| --- | --- | --- | --- |
| A0 | Observe | Report findings and hypotheses | Human |
| A1 | Propose | Open a pull request or a proposal | Human merges |
| A2 | Ship with canary | Merge and release behind a flag to a small cohort, auto-rollback | Policy, human can veto |
| A3 | Ship | Release fully after canary passes | Policy |

A change class moves up one level only after a recorded run of clean changes at the level
below (default: 20 consecutive changes with no rollback and no human correction). Any
incident drops the class back to A1. Authentication, payments, data deletion and schema
changes are capped at A1 in v0.1.

## 5. Openness

- Code under MIT. Documentation and research notes under CC BY 4.0.
- Experiment records, including failed ones, are public in [`experiments/`](experiments/).
- Datasets we publish (for example, anonymized replay-derived test suites) state their
  source, consent basis and scrubbing method.

## 6. Governance

- v0.1: one maintainer (Shirish Kadam) with final say.
- From the first external contributor with three merged pull requests: decisions that change
  this charter, the safety constitution or the default stack need a second maintainer's
  approval.
- Architecture decisions are recorded as ADRs in [`docs/decisions/`](docs/decisions/).

## 7. AI use

This project is built with heavy AI assistance. Commits and experiment records state which
models were used. Humans remain responsible for every merged change and published claim.
