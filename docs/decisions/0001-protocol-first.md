# 0001: Protocol first, JavaScript reference implementation

- **Status:** Accepted
- **Date:** 2026-10-20
- **Deciders:** Shirish Kadam

## Context

The goal is a platform-agnostic framework. Writing and maintaining SDKs for many languages and
frameworks would consume the project before any research happens.

## Options

| Option | Pros | Cons |
| --- | --- | --- |
| Multi-platform SDKs from day one | Broad reach | Huge maintenance, no research time |
| JS only, own formats | Fast | Locks out other platforms later |
| Protocols plus one JS reference | Reach comes from standards; small surface | Depends on maturing standards |

## Decision

Define Ultrastable's own primitives (jobs manifest, ledger, policy) as JSON Schemas. Use
existing protocols for everything else: OpenTelemetry for signals, OpenFeature for flags,
A2UI for generated UI. Build the reference implementation in TypeScript.

## Consequences

- Any platform that speaks these protocols can join without a dedicated SDK.
- We must track the evolution of OTel feature flag conventions and A2UI, which are still
  marked experimental or pre-1.0.
