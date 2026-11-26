# Mechanism map

| Mechanism | Active implementation |
|---|---|
| Identity / tone | `_system/SOUL.md` and onboarding |
| Owner adaptation | `me/PROFILE.md`, selected work packs |
| Durable memory | `_system/MEMORY.md` plus linked evidence |
| Context selection | bounded boot and optional context hook |
| Cross-session continuity | `_system/session.md` plus optional loader |
| Automatic filing | AGENTS.md / CLAUDE.md, conventions and blank templates |
| Commitments / priorities | `_system/open-asks.md` and `_system/board.md` |
| Dedicated work | `.claude/commands/`, usable as Markdown in either client |
| Design and interface work | `Design/00 Framework/`, website and unslop skills |
| Security work | local skill instructions; scanning tools installed separately |
| Dedup / backlinks / source audit | maintenance workflow |
| Graph extraction | full maintenance, graph.json when generated |
| Tool boundaries | `_system/accounts.md` and operating manual |
| Personal hierarchy | blank domain folders with README purpose notes |

The upstream skill collection is preserved under `reference/upstream-skills` with attribution. Global plugin installations, credentials, browser profiles, private deployments and live automation are not copied. See SETUP.md for dependencies.

The optional context hook uses bounded lexical matching, not embeddings. Session continuity depends on the assistant writing its handoff. There is no always-running process or automatic cloud backup. Live client behavior and external integrations require verification in the owner's environment.
