# Glossary

| Term | Meaning |
| --- | --- |
| **Job** | A task users come to the app to complete, with a measurable success condition |
| **Jobs manifest** | The file declaring jobs, success criteria, guardrails and invariants. The fitness function. |
| **Guardrail** | A metric that must stay inside a range. Breaching it triggers rollback. Ashby's "essential variable". |
| **Invariant** | Something no loop may change: privacy rules, legal copy, accessibility minimums, prices |
| **Signal** | A structured observation from a source (error cluster, replay pattern, survey theme, CVE) |
| **Hypothesis** | A ledger entry stating what is wrong, why, the proposed change and its predicted impact |
| **Candidate** | One proposed change produced by the mutator |
| **Ledger** | Append-only record of every hypothesis, candidate, decision and measured outcome |
| **Change class** | A category of change with its own autonomy level |
| **Autonomy level** | A0 Observe, A1 Propose, A2 Ship with canary, A3 Ship |
| **Senses** | Components that read signals; never write |
| **Mutator** | Sandboxed agent that produces candidates |
| **Selector / verifier** | Judges candidates against tests, replays, synthetic users and invariants |
| **Deployer** | Policy code that ships or rolls back; contains no language model |
| **Replay-derived test** | An automated browser test generated from a real, scrubbed user session |
| **Synthetic user** | An agent persona that attempts jobs on staging to estimate a candidate's effect |
| **Population** | Several candidate variants live at once, each with a share of traffic |
| **Genome** | The intent spec (jobs, invariants, catalog) from which code and UI could be regenerated |
| **Phenotype** | The running code and UI, including per-user adaptations |
| **Lethal trifecta** | Private data, untrusted content and external communication in one agent (Willison) |
| **Ultrastability** | Ashby's two-loop adaptation: ordinary feedback, plus structural change when essential variables leave their range |
