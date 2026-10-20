# Security policy

Ultrastable is designed to let software change itself. Bugs that let untrusted input steer
those changes are the most serious class of issue this project can have.

## Reporting

Report vulnerabilities privately through GitHub's "Report a vulnerability" button on this
repository. Do not open a public issue.

Include what component was affected (senses, diagnostician, mutator, selector, deployer),
the input used, and what the system did. We aim to reply within 7 days.

## In scope

- Prompt injection through any signal (feedback, survey text, replays, error messages,
  dependency metadata) that changes what the mutator or deployer does
- Any path that lets one component hold private data, untrusted input and deploy rights
- Ledger or policy tampering
- Leakage of real user data into sandboxes, tests or commits

## Red-team results

Injection cases we find ourselves are kept as a test suite (see
`experiments/05-immune-system.md`). Cases from reporters are added after a fix ships, with
credit if wanted.
