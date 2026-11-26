# Setup and connection

## Install the actual vault
The downloaded repository is a distribution. `reference/` contains background material, and `template-vault/` contains the complete starting hierarchy, including hidden `.claude` and `.agents` directories. The three folders at the top of a download are not the installed vault.

1. Extract the complete ZIP, or clone the repository.
2. Open a terminal in the extracted repository (the folder containing `install.py`).
3. Run `python3 install.py ../my-brain` on macOS/Linux, or `py install.py ../my-brain` on Windows. Python 3.9 or newer is required. Choose a new or empty destination.
4. Open the generated `my-brain` folder in Claude Code or Codex. If using Obsidian, choose **Open folder as vault** and select that same folder.
5. Say **Set up my brain.** Choose the assistant name and describe your own work.

No folders need to be recreated manually. Optional Claude context hooks can be enabled at initial installation by adding `--enable-hooks`; these are not Codex hooks. No background schedules are installed.

## Updating an existing installation
Download the latest distribution or run `git pull` in its clone. Install into a new empty folder first. Compare its system files with your existing vault and merge reusable updates while preserving your profile, SOUL, MEMORY, board, accounts, journal and other records. The installer intentionally refuses a nonempty destination. Do not replace a populated vault with the template.

## Tools and plugins
The repository contains Markdown operating instructions, local workflow skills and selected supporting scripts. A tool mentioned by a skill is usable only after it is installed, connected and available in the current client.

| Capability | Separate setup |
|---|---|
| Claude Code / Codex | Install your chosen client and sign in with your own account. |
| Obsidian | Optional viewer/editor; open the installed vault folder. |
| Browser automation | Connect a browser tool supported by the client and record the intended account in `_system/accounts.md`. |
| Research and search | Use the client's available search tools; paid providers require your own account. |
| Design components | HeroUI, shadcn and 21st tooling are optional project dependencies/integrations, installed as needed. |
| Security scanning | Strix and related services require separate installation/access and an explicitly authorized target. |
| CRM, mail, meetings and enrichment | Connect your own provider accounts; Clay, Fathom and mail integrations are not preconnected. |
| Hosting and source control | Authenticate your own GitHub/hosting accounts and choose project-specific destinations. |
| Global workflow packs | GSD, gstack, Superpowers, document/media and marketing plugin collections are external installations; this repo does not bundle the original machine's global plugin cache or promise their availability. |

Record confirmed tool/account mappings and credential locations, never tokens or passwords. Review a chosen provider's current official installation instructions when adding it. Paid plans, installed apps, running automation, browser sessions and existing third-party subscriptions do not transfer with a vault.
