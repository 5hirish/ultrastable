# 0002: PostHog as sensory system and baseline, not a competitor

- **Status:** Accepted
- **Date:** 2026-10-20
- **Deciders:** Shirish Kadam

## Context

PostHog ships analytics, replays, error tracking, surveys and flags under an MIT core, and
in 2026 launched Self-driving: scouts and signal sources feed reports, which become pull
requests that a human merges, followed by measurement. That covers most of the L2 loop.

## Options

| Option | Pros | Cons |
| --- | --- | --- |
| Build our own signal and L2 pipeline | Full control | Duplicates a well-funded open product |
| Ignore PostHog, use separate tools | Vendor neutral | More integration, weaker data joins |
| Use PostHog as senses and as the baseline | Fast start, honest comparison | Dependence on one vendor's roadmap |

## Decision

PostHog is the default sensory system and the baseline every experiment must beat. Its
signals and reports are inputs to our diagnostician. Adapters stay narrow so another source
can replace it.

## Consequences

- Ultrastable's value must come from what PostHog does not do: L1 individualization,
  populations, synthetic-user verification, separation of powers, cross-app learning.
- If PostHog ships one of those, we adopt it and move on.
- Self-hosted PostHog has a practical ceiling around 100k events per month; the testbed may
  need PostHog Cloud.
