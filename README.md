# Second Brain Starter

A complete reusable vault foundation for Claude Code and Codex: folder hierarchy, memory, operating rules, dedicated workflows, filing conventions, templates, design method and local skills. Personal records start empty. Choose the assistant's name and describe your own work during onboarding.

Built on the Second Brain framework by Asadulelah. See LICENSE and retained third-party attribution.

## Download and install

Download and extract the **whole repository**, then open a terminal in the folder containing `install.py`:

```sh
python3 install.py ../my-brain
```

On Windows:

```powershell
py install.py ../my-brain
```

Requires Python 3.9+ and an installed Claude Code or Codex client. The destination must be new or empty. Open the generated **my-brain** folder in your AI client and say **Set up my brain.** For Obsidian, open that same folder as a vault.

The repository's `reference/` directory is supporting reading. The working hierarchy lives in `template-vault/` and is copied automatically, including hidden client instruction folders. You do not have to create the folders by hand.

Optional Claude context hooks: add `--enable-hooks` during initial installation. These do not run in Codex; no background service is installed.

## Included

- Identity, owner profile, durable memory, project board, commitments and session continuity.
- Journal, people, clients, pipeline, projects, knowledge, strategy, finance, raw sources, attachments, deliverables and build folders.
- Daily briefing, call prep/debrief, follow-up, research, offers, outreach, content, decks, handoff and maintenance workflows.
- Detailed filing conventions and blank record templates.
- Shared interface design method, website workflow, unslop and local security workflow instructions.
- Optional domain packs for SEO, marketing, science and website work.

Your own AI clients, integrations, global plugins and accounts must be installed or connected separately. Instructions do not transfer access to external services. See [setup and connection](docs/SETUP.md), [mechanism map](docs/MECHANISMS.md) and [verification](docs/VERIFICATION.md).

New to second brains? Read the [Second Brain Field Guide](docs/SECOND-BRAIN-GUIDE.md) for the basics, daily routines, prompt examples and advanced workflows.

Keep the installed personal vault separate from this public distribution. Model clients may send loaded content to their providers; local Markdown does not imply offline inference.
