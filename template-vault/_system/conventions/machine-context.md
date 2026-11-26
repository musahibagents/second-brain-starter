---
type: convention
status: active
---

# Machine Context

Before machine-specific work inspect actual tools, current working directory and OS; optionally read a local machine profile when one exists. Never assume a default Windows/Mac/server identity from a missing profile. Resolve paths from the current environment rather than another operator’s absolute paths. Verify available browser sessions, credentials and binaries before relying on them. Record environment-dependent outcomes with a machine label. Keep local machine configuration and secrets outside shared version control. Missing capabilities are explicit blockers for those actions, not proof that the same task was never done elsewhere.
