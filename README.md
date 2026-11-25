# Second Brain Starter
A portable personal assistant with a file-based memory. Choose its name, explain your work, and let it adapt through conversation.

Built on the Second Brain framework by Asadulelah. This distribution generalizes the operating mechanisms into a portable Claude Code and Codex starter. See LICENSE.

## Install
Requires Python 3.9+ and an installed Claude Code or Codex client. Obsidian is optional.

1. Download or clone this starter.
2. Run `python3 install.py /path/to/my-brain` (Windows: `py install.py C:/path/to/my-brain`). The destination must be absent or empty.
3. Open the resulting folder in Claude Code or Codex and say: **Set up my brain.**
4. Choose its name, describe your work and preferences. Onboarding writes your profile and working rules.

The installed brain is a separate private folder. Keep personal records out of this distribution repository. Model clients may send loaded content to their providers; local Markdown storage does not imply offline inference.

## Included mechanisms
Identity and user profile; concise durable memory; project board and commitments; automatic filing and backlinks; sourced research and decision logs; progressive onboarding; session handoff; context selection; maintenance, deduplication, reconciliation, and typed graph guidance; portable Claude and Codex adapters.

Optional Claude hooks load session state and select relevant notes. Enable them with `python3 install.py /path/to/my-brain --enable-hooks` during initial installation. Codex uses the same files and explicit session handoff; Claude hooks do not run in Codex. No background schedule is installed. Maintenance runs on request.

Optional work packs cover SEO, marketing, scientific research, and website projects. Onboarding selects and adapts packs from the owner's explanation. Any other domain can be added using the same structure.

See `docs/MECHANISMS.md` for the mechanism map. `reference/upstream-skills/` preserves the original framework workflows as reference; active workflows live in the installed vault and do not require those optional integrations.
