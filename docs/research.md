# Research landscape

Last reviewed: 2026-10-20. This file summarizes prior art and expert opinion in our own words.
Follow the links for the originals. Update it when something important changes, and date the
change.

## 1. Autonomic computing: the 25-year-old version of this idea

IBM's autonomic computing vision (2001 to 2003) proposed self-configuring, self-healing,
self-optimizing and self-protecting systems, organized around the MAPE-K loop: Monitor,
Analyze, Plan, Execute over shared Knowledge. It stalled because analysis and planning had to
be hand-written rules. Recent surveys argue LLMs can strengthen every phase of the loop.

**Takeaway for us:** Ultrastable is MAPE-K with models doing Analyze and Plan, and the ledger
as Knowledge. We should use the self-adaptive systems literature (SEAMS community) for
vocabulary and evaluation methods instead of reinventing them.

- [The Vision of Autonomic Computing: Can LLMs Make It a Reality?](https://arxiv.org/abs/2407.14402)
- [Exploring the Potential of LLMs in Self-adaptive Systems](https://arxiv.org/abs/2401.07534)
- [Generative AI for Self-Adaptive Systems: State of the Art and Research Roadmap](https://arxiv.org/abs/2512.04680)

## 2. Cybernetics: Ashby's ultrastability

W. Ross Ashby's Homeostat (1948) and *Design for a Brain* (1952) describe an ultrastable
system: an inner feedback loop for normal disturbance, and an outer loop that changes the
system's own structure only when an essential variable leaves its safe range. This is the
origin of the project's name and of the jobs manifest's guardrails.

## 3. Self-improving agents

- **Darwin Gödel Machine** (Sakana AI and UBC, ICLR 2026). A coding agent rewrites its own
  code, keeps an archive of variants and validates each change on benchmarks. It went from
  20% to 50% on SWE-bench. Open-ended exploration over an archive beat greedy hill climbing.
  [Paper](https://arxiv.org/abs/2505.22954) · [Sakana write-up](https://sakana.ai/dgm/)
- **Harness Updating Is Not Harness Benefit** (KDD 2026). The quality of self-updates barely
  depends on the updater model's strength (a 9B open model's updates gained about as much as
  a frontier model's), while the agent using the update matters a lot. Unverified updates
  often silently hurt. [Paper](https://arxiv.org/abs/2605.30621)
- **Harness engineering survey** by Lilian Weng (July 2026) collects the 2026 wave of
  self-evolving harness work. [Post](https://lilianweng.github.io/posts/2026-07-04-harness/)
- **AlphaEvolve** shows evolutionary code search works when an automated evaluation function
  exists. That function is exactly what products lack.

**Takeaway for us:** the mutation engine can be cheap and open. The verifier is the hard,
valuable part. Populations beat single candidates.

## 4. Frontier lab view: recursive self-improvement

Anthropic's Institute (September 2026) reports that over 80% of merged code at Anthropic is
written by Claude, and that Claude now handles underspecified engineering problems well. The
remaining gap is judgment in choosing goals. Their speedup experiments work because goals and
metrics are fixed in advance.
[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement)

**Takeaway for us:** L2 (fixed goals) can be highly autonomous now. L3 (choosing goals)
keeps a human as director.

## 5. Generative and adaptive UI

- **OpenAI Intelligent UI** (GPT-6, October 2026): a library of native streamable components
  plus a compiler; the model decides composition. OpenAI states the direction plainly:
  software should adapt to people. [Announcement](https://openai.com/index/gpt-6-for-everyone/)
- **Google Research, "Generative UI: LLMs are Effective UI Generators"** (November 2025):
  raters strongly preferred generated UI over plain LLM output when speed was ignored, but
  human expert sites were still preferred most.
  [Blog](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/)
- **Protocols:** A2UI (Google, declarative component streams, data not code), MCP Apps
  (sandboxed iframe UI from tools) and AG-UI (CopilotKit, the runtime transport beneath them).
  The ecosystem has converged on agents emitting allow-listed components rather than raw code.
  [A2UI v0.9](https://developers.googleblog.com/a2ui-v0-9-generative-ui/) ·
  [AG-UI specs overview](https://docs.ag-ui.com/concepts/generative-ui-specs)
- **Adaptive UI research:** Gajos et al. (CHI 2008) found both predictability and accuracy
  raise satisfaction, with accuracy mattering more for performance. Wrong adaptation is worse
  than none. [Paper](https://www.eecs.harvard.edu/~kgajos/papers/2008/gajos08predictability.shtml)

**Takeaway for us:** L1 runs over a component catalog via A2UI, adapts at session boundaries,
and favors accuracy over novelty.

## 6. Expert opinions

- **Jakob Nielsen** sees AI as the third UI paradigm, intent-based outcome specification, and
  predicts second-generation generative UI, regenerated on every visit, in about five years.
  NN/g calls the resulting practice outcome-oriented design: designers set goals and
  constraints rather than layouts.
  [Individualizing UX](https://uxtigers.com/post/individualizing-ux) ·
  [Accessibility and generative UI](https://www.uxtigers.com/post/accessibility-generative-ui)
- **Andrej Karpathy** frames Software 3.0: prompts and context as the program. His 2026
  MenuGen demo replaced a full-stack app with one multimodal call, and he has argued many
  existing apps should not exist as apps at all. He also says pure vibe coding is unsafe for
  serious web apps; agentic engineering with supervision is the default.
  [Summary](https://www.aibuilderclub.com/blog/karpathy-software-3-0)
- **Ink & Switch and Geoffrey Litt** argue for malleable software: gradual paths from using to
  changing tools, interoperation through shared data, and communities that share changes.
  Litt warns that strong coding agents can erode the mental models people need to steer.
  [Malleable software essay](https://www.inkandswitch.com/essay/malleable-software/)
- **Simon Willison** names the lethal trifecta: private data, untrusted content and external
  communication in one agent means it can be tricked into leaking. Guardrails that block 95%
  of attacks are a failing grade; the fix is architectural.
  [The lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)

## 7. Industry: what already ships

- **PostHog Self-driving** (open beta, 2026): scouts (scheduled agents, written as readable
  SKILL.md files) and signal sources (errors, replays, Zendesk, GitHub Issues, Linear) emit
  signals, which are grouped into reports, turned into pull requests, merged by a human and
  then measured. An LLM classifier drops suspicious signals to resist injection. Billed per PR.
  Replay Vision (GA August 2026) scores frustration and summarizes sessions.
  [Self-improving loop docs](https://posthog.com/docs/self-driving/self-improving-loop) ·
  [What is a scout?](https://posthog.com/blog/what-is-a-scout)
- **Warp** (October 2026) describes proactive agents for bug fixes, agent self-improvement and
  product work. [Post](https://www.warp.dev/blog/self-improving-software-proactive-agents)
- **Sentry Seer** analyzes issues and opens PRs (Sentry itself is source-available under FSL,
  not OSI open source).
- **OpenHands, Hermes Agent** and others provide open coding and self-improving agents we can
  plug in rather than rebuild.

**Takeaway for us:** L2 with a human merge is solved enough to use, not to compete with.
Our ground is everything they do not attempt: L1 individualization, populations of
variants, pre-release fitness from synthetic users, separation-of-powers security, and
learning shared across apps.

## Open questions we have not found answers to

1. Is there any published evidence that user simulators trained on replays predict real A/B
   outcomes for UI changes?
2. What is a reasonable consent model for per-user adaptation under GDPR?
3. How should adaptations be shared across apps without leaking one app's user behavior?
