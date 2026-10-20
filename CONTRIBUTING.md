# Contributing

Thanks for helping. Ultrastable needs four kinds of contributors:

- **Product and HCI researchers** to design experiments and judge adaptive UI results
- **Engineers** to build adapters, the verifier and the reference implementation
- **Security researchers** to red-team the separation of powers
- **Teams with a live app** willing to act as testbeds

## Before you start

1. Read `CHARTER.md`, especially the safety constitution.
2. Read `ROADMAP.md` and pick an open step, or propose a new experiment.

## Workflow

1. Open an issue describing the change or experiment.
2. Work on a branch named `exp/<NN-slug>`, `docs/<topic>` or `feat/<topic>`.
3. Run `python tools/validate.py`.
4. Open a pull request. Experiment proposals need one reviewer to agree the hypothesis,
   metric and kill signal before work starts.

## What we will not accept

- Experiments without a kill signal, or with goalposts changed after starting
- Real user data, credentials or unscrubbed replays
- Features that give one component private data, untrusted input and deploy rights together
- Dependencies on non-OSI tools as defaults (adapters are fine)

## AI assistance

You may use AI tools. List the models used in the PR and in any experiment record. You remain
responsible for every claim and line of code.
