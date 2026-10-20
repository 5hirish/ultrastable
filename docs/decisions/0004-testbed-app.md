# 0004: Testbed app for Phase 1

- **Status:** Proposed
- **Date:** 2026-10-20
- **Deciders:** Shirish Kadam

## Context

Phase 1 needs one real app with real users. Step 3 needs enough replays per job to build a
meaningful test suite, and step 4 needs past changes with known outcomes.

## Requirements

- Live users, ideally 1,000 or more sessions per month
- Owner willing to let agents open PRs against it
- 3 to 5 clear jobs with measurable success events
- Web front end in JavaScript or TypeScript
- PostHog installable (Cloud or self-hosted)

## Options

| Option | Pros | Cons |
| --- | --- | --- |
| An own product | Full control, no client risk | May have low traffic |
| A client product | Real traffic | Needs client consent and a data agreement |
| A purpose-built demo app | Safe | Synthetic users only, weak evidence |

## Decision

To be decided before step 0 starts.
