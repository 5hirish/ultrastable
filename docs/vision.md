# Vision

## The problem

Software is shipped as a fixed appliance. People adapt their work to it, not the other way
round. When it fails them, they file feedback and wait. Meanwhile, every product already
collects the signals needed to know what is failing: analytics, replays, errors, surveys,
performance traces. Those signals sit in dashboards until a human has time to read them.

AI has changed two things. Agents can now write, test and ship code for well-specified
problems. And interfaces can be generated at runtime (OpenAI's Intelligent UI, Google's
generative UI work, the A2UI and MCP Apps protocols). What is missing is the system that
connects the signals to the changes with evidence, safety and user consent in between.

## The bet

Software can run its own improvement loop if three things exist:

1. **A declared purpose.** The app states its jobs, what success looks like for each, and
   what must never break. Without this, "improve" collapses into "increase engagement".
2. **A trustworthy verifier.** Every candidate change is checked against real past behavior
   before it reaches users, then measured after. Self-modification without verification
   mostly makes things worse.
3. **An architecture that cannot be talked into harm.** No single component that reads user
   content can also deploy.

## Three loops

- **L1 Adapt:** the interface shapes itself per user or segment, over a fixed component
  catalog, at session boundaries, explainable and reversible.
- **L2 Heal:** bugs, crashes, slow paths and vulnerable dependencies get fixed with a
  reproduction test first.
- **L3 Evolve:** new features, flows, schema and infra are proposed from patterns in the
  ledger. A human chooses.

This matches what the frontier labs report: agents are strong at execution against fixed
goals (L2) and still weak at choosing goals (L3). L1 is bounded less by model capability and
more by what decades of adaptive UI research say about predictability.

## Software as an organism

The long-term model. Each organ is its own research question.

| Organ | Idea | Research question |
| --- | --- | --- |
| **Genome** | The source of truth is an intent spec: jobs, invariants, component catalog. Code and UI are a phenotype compiled from it. | Can an app be regenerated from its genome with equivalent behavior on replayed sessions? |
| **Population** | Keep an archive of variants per segment, give each a share of traffic, select on job completion. | Does open-ended search beat one greedy PR at a time? |
| **Synthetic users** | Simulators trained on the app's own replays run candidate variants before real users see them. | Does simulator ranking predict real ranking? |
| **Phenotype contract** | Per-user adaptation that is proposed, explained and reversible, not silent. | Does proposed adaptation beat static and silent adaptation on trust and completion? |
| **Immune system** | Separation of powers so no component holds the full lethal trifecta. | Can red-team injections ever reach the deployer? |
| **Gene pool** | Verified adaptations shared across installations as reusable patterns. | Do improvements transfer between apps with similar jobs? |
| **Metabolism** | Every mutation has a compute cost; fitness is job completion minus cost. | Does each loop pay for itself? |

## What we are not

- Not an analytics product. PostHog and others already do that well.
- Not a coding agent. Many exist; we orchestrate them.
- Not a promise of fully autonomous software. Autonomy is earned per change class, with
  evidence, and some classes may never earn it.

## Where this sits between two camps

One camp (Karpathy's Software 3.0, Nielsen's second-generation generative UI) expects
interfaces to be generated on demand for each person. The other (Ink & Switch, Geoffrey Litt)
warns that software changing itself without the user's participation removes their agency.
Ultrastable tries to hold both: the system proposes, the user owns.
