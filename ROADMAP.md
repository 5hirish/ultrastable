# Roadmap: the experiment ladder

Ultrastable moves in small, falsifiable steps. Each step is useful on its own even if the
project stops there, and each one removes a risk for the next.

## Rules for every step

- Takes one to two weeks.
- Has one metric and one decision at the end: **continue, adjust or kill**.
- Leaves something reusable behind: a spec, a tool or a dataset.
- Gets written up in [`experiments/`](experiments/) and summarized publicly, including failures.

## The testbed

All early steps run on one real app with real users, instrumented with PostHog. The app must
have enough sessions for replays to be meaningful by step 3.

> **Open decision:** testbed app not chosen yet. Record the choice in
> [`docs/decisions/`](docs/decisions/) before step 0 starts.

## Phase 1: build the evidence base

| Step | Build | Done when | Unlocks | Record |
| --- | --- | --- | --- | --- |
| 0. Baseline | PostHog plus Self-driving on the testbed, untouched for 2 weeks | Numbers exist for job completion, error rate and PR merge rate | Something to beat | [00](experiments/00-baseline.md) |
| 1. Jobs manifest v0 | Hand-write 3 to 5 jobs with success events and guardrails | A daily view shows completion rate per job | The fitness function exists | [01](experiments/01-jobs-manifest.md) |
| 2. Ledger v0 | A plain log of every change, human or agent, with hypothesis and measured impact after 7 days | 10 entries have measured outcomes | Memory, plus history to test against | [02](experiments/02-ledger.md) |
| 3. Replay to test | Top 20 sessions per job converted into Playwright tests in CI | The suite catches a regression planted on purpose | Automated verification | [03](experiments/03-replay-to-test.md) |
| 4. Synthetic users v0 | Agent personas run the jobs on staging | Their results match real outcomes on 2 to 3 past ledger changes | Testing before real traffic | [04](experiments/04-synthetic-users.md) |
| 5. Immune system v0 | Sandboxed mutator with no network, deployer as pure flag policy | 10 red-team injections, none reach the deployer | Safe autonomy | [05](experiments/05-immune-system.md) |
| 6. First population | 3 variants of one screen behind flags, selected on job completion | A winner is chosen on evidence, or we learn why not | Evolution, not just fixes | [06](experiments/06-first-population.md) |
| 7. First adaptation proposal | One in-app suggestion offered to users ("Want a button for this?") | Acceptance rate and job impact measured | L1 with user agency | [07](experiments/07-adaptation-proposal.md) |

Steps 0 to 2 need almost no engineering and can start immediately.

**Gating steps:** 4 (is the fitness function trustworthy?) and 5 (is the architecture
secure?). If either fails, Phase 2 is paused, not forced.

## Phase 2: the bold bets (only after steps 4 and 5 pass)

| ID | Experiment | Hypothesis | Kill signal |
| --- | --- | --- | --- |
| E1 | Genome extraction | An agent infers a jobs and invariants spec from an existing app plus replays, and a human accepts it with light edits | Over 50% of the spec needs rewriting |
| E2 | Synthetic users at scale | Simulators trained on replays rank UI variants the way real users do | Top-2 ordering no better than chance |
| E3 | Population vs single PR | An archive of variants beats single greedy fixes on job completion over 4 weeks | No better than the PostHog baseline |
| E4 | Adaptation contract | Proposed adaptation beats both static UI and silent adaptation on trust and completion | Proposals mostly declined, or silent adaptation wins |
| E5 | Immune system at scale | Injections through feedback, replays and errors never reach the deployer | Any injection reaches production |
| E6 | Regeneration | The app rebuilt from its genome passes the replay regression suite | Behavior drifts on any critical job |
| E7 | Shared gene pool | Verified adaptations transfer across apps with similar jobs | Transferred adaptations lose to local ones |

## What would make us stop the whole project

- Step 4 fails twice with different simulator designs, and no other pre-release fitness
  signal is found. Without one, Ultrastable is PostHog Self-driving with extra steps.
- Step 5 shows injections reaching the deployer that we cannot close architecturally.
- After step 6, cost per verified improvement stays above the cost of a contractor doing the
  same change by hand.
