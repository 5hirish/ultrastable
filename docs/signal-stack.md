# Signal stack

Every default tool must be OSI open source and self-hostable. Licenses were checked on
2026-10-20; recheck before depending on a tool.

| Signal | Default tool | License | Notes |
| --- | --- | --- | --- |
| Product analytics, funnels, paths | PostHog | MIT core (the `ee/` directory is separately licensed) | Self-hosted hobby deploy is meant for about 100k events per month |
| Session replay | PostHog | MIT core | Source for replay-derived tests and simulator training |
| Errors and exceptions | PostHog error tracking | MIT core | Keeps errors next to replays and flags |
| Errors (alternative) | GlitchTip | MIT | Accepts Sentry SDK events. Sentry itself is FSL, not open source |
| Surveys and satisfaction | PostHog surveys | MIT core | In-app CSAT and open text, treated as untrusted |
| Feature flags and rollout | OpenFeature + flagd | Apache-2.0 | Vendor-neutral flag API; PostHog flags via provider |
| Traces and performance | OpenTelemetry | Apache-2.0 | Feature flag semantic conventions link changes to telemetry |
| Dependency vulnerabilities | OSV-Scanner | To verify | |
| Code scanning | Semgrep CE | To verify | |
| Container and config scanning | Trivy | To verify | |
| Generated UI | A2UI | To verify | Declarative component streams, data not code |
| Coding agent | Pluggable: Claude Code, OpenHands, Aider | Varies | Called only from the sandboxed mutator |

## Relationship with PostHog Self-driving

PostHog Self-driving already runs signals to reports to pull requests to measurement for L2
and early L3. We treat it as two things:

1. **A sensory system.** Its signals, scouts and reports are an input to our diagnostician.
2. **The baseline.** Every experiment compares against Self-driving on the same app.

We do not rebuild what it does. See ADR [0002](decisions/0002-posthog-as-senses-and-baseline.md).
