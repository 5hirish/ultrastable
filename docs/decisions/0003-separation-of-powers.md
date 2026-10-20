# 0003: Separation of powers to break the lethal trifecta

- **Status:** Accepted
- **Date:** 2026-10-20
- **Deciders:** Shirish Kadam

## Context

A self-evolving app reads untrusted text (feedback, replays, error messages), holds private
data, and can deploy. An agent with all three can be tricked by a crafted input into leaking
data or shipping harmful changes. Prompt-level defenses are probabilistic.

## Options

| Option | Pros | Cons |
| --- | --- | --- |
| One agent with guardrail prompts and a classifier | Simple | Fails a small share of the time, which is enough |
| Human approval for everything | Safe | No autonomy, defeats the research |
| Split roles so no component holds all three capabilities | Architectural guarantee | More components, more plumbing |

## Decision

Four roles: senses (read, no write), mutator (sandboxed, synthetic data, no network),
selector (different model or deterministic), deployer (policy code, no LLM). An injection
filter sits in front of the senses as defense in depth, not as the main defense.

## Consequences

- Any feature that would merge two roles needs a new ADR and a red-team run.
- The mutator cannot see real user data, so replay-derived tests must be scrubbed first.
