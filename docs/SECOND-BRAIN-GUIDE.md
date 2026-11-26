# The Second Brain Field Guide

An approachable guide to using your personal knowledge system with Codex or Claude.

## Start here

A second brain is a set of notes and working rules that helps an AI assistant understand your context across sessions. The files live in a folder you control. Codex or Claude reads the relevant files when you work in that folder, then helps you capture decisions, find context, and move tasks forward.

It is not a magic database that knows everything, and it does not automatically make you productive. It works when useful context is captured, kept findable, reviewed, and connected to the work you do. Start small. You do not need to understand every folder before using it.

## The four parts

1. **You and your working rules** — `me/PROFILE.md` describes your work and preferences. `_system/SOUL.md` describes how your assistant should behave.
2. **Memory and current work** — `_system/MEMORY.md` holds a short index of durable facts. `_system/board.md` and `_system/open-asks.md` track active priorities and commitments.
3. **Reference notes** — `people/`, `ventures/`, `knowledge/`, `strategy/`, and other folders keep information by topic. `journal/` records dated events; `summaries/` distills sources.
4. **Operating instructions** — `AGENTS.md` and `CLAUDE.md` tell the coding assistant how to work in this folder. `_system/workflows/` and `.claude/commands/` provide repeatable procedures. Local skills explain specialized work.

The Markdown files are the durable memory. The AI model is the reasoning partner. Your terminal or editor is where you open the vault. Obsidian is optional: it displays and edits the same files but is not required for Codex or Claude.

## First session

Open the **installed vault folder** (the one containing `AGENTS.md` and `CLAUDE.md`) in Codex or Claude Code. Sign in to your AI client. Then say:

> Set up my brain. Ask me one question at a time. Help me choose your name, explain my work and goals, and set up only the folders and tools I need. Do not invent facts.

Answer in your own words. You can skip anything. The assistant should fill in your profile and working preferences from what you confirm. Check those files afterward and correct anything that sounds wrong.

## How to talk to it

You do not need special prompt syntax. Say what you want in ordinary language and include useful context. A good request usually has four parts:

**Outcome + context + constraints + next action.**

For example: “Help me prepare for my call with Priya tomorrow. Search the vault for our last conversation, summarize her goals and unresolved questions, and make a one-page call brief. Flag anything we do not know.”

Be clear about whether you want discussion, a draft, or a build. Ask it to search the vault before starting from scratch. Tell it to save useful outcomes when you want them remembered. For external actions such as sending a message or publishing, state the action explicitly and check the result yourself.

### Prompt examples

- **Capture:** “I’m going to dictate rough notes. Turn them into a concise journal entry, keep uncertainty visible, and add the decisions and next actions to the right pages.”
- **Find context:** “Search my vault for the latest decision on the website redesign. Give me the source page and tell me if the notes conflict.”
- **Think:** “I’m considering [decision]. Ask me questions one at a time, challenge weak assumptions, and end with options and tradeoffs. Don’t edit files yet.”
- **Plan:** “Turn this outcome into a plan with milestones, owners, risks, and a first next action. Check my board for conflicts.”
- **Draft:** “Draft a reply to this message using my tone and the project notes. Do not send it.”
- **Build:** “Build [specific outcome] in [project]. First inspect the existing code and relevant notes, then implement it and report what you changed.”
- **Remember:** “This is a durable preference: [preference]. Update my profile and link it to the related workflow.”
- **Review:** “What open commitments are overdue or missing a next action? Show the file evidence; don’t assume silence means nothing happened.”

## A simple daily rhythm

### Start of day (5 minutes)

Ask: “Give me a brief from my board and recent journal. What is due, what needs follow-up, and what are the three most useful next actions? Distinguish recorded facts from guesses.” Choose one priority and add a clear next action to the board.

### During work

Open the vault in the AI client and work in the relevant project folder if you have one. Before a meeting, ask for a brief. After it, capture the decisions, commitments, and who owns each next step. When you learn a durable fact, ask the assistant to file it and link it to the relevant person or project.

### End of day (3 minutes)

Ask: “Summarize what changed today, file durable decisions, update completed or changed commitments, and prepare a short handoff for next time. Leave uncertain items marked as uncertain.” Review the proposed changes if the assistant has made any assumptions.

## How to keep the brain useful

- **Capture decisions and context, not every message.** Distill raw information into what will help future work.
- **Keep one canonical page per important person, project, or idea.** Search before creating duplicates.
- **Link related notes.** A journal entry about a project should point to that project’s page.
- **Keep memory short.** `_system/MEMORY.md` is an index to durable facts, not a transcript archive.
- **Track commitments with an owner and next action.** A vague “follow up” is hard to act on; “Email Sam the revised scope by Thursday” is usable.
- **Correct errors quickly.** Say “That’s wrong; the correct fact is…” and ask it to update the source page and any affected summary.
- **Review stale information.** Old dates and decisions should remain marked as historical, not silently treated as current.

## How the folders fit together

| Folder | Use it for |
|---|---|
| `_system/` | Working rules, memory, board, templates, workflows and setup |
| `me/` | Your profile and preferences |
| `journal/` | What happened on a date, including meetings and decisions |
| `people/` | People pages and relationship context |
| `ventures/` | Clients, prospects, products and projects |
| `knowledge/` | Durable concepts and frameworks |
| `summaries/` | Distilled books, articles, videos and other sources |
| `strategy/` | Plans, positioning, offers and research that guide action |
| `inbox/` | Unsorted notes waiting to be processed |
| `raw/` | Source material kept for reference |
| `outputs/` | Deliverables created from the work |

You do not need to fill every folder. Create pages when there is something real to store.

## Advanced use

### Workflows and commands

The included workflows make common tasks repeatable. In Claude Code, command files can appear as slash commands. In Codex, request the same workflow in plain language: “Prepare for my call,” “Debrief this meeting,” “Research this topic,” or “Run maintenance on my brain.” The operating manual routes the request to the matching instructions.

### Context selection

Do not ask the AI to read the entire vault for every task. Name the project or outcome and ask it to search for relevant context. The boot instructions load a small amount of current state; the assistant should open deeper files only when the task needs them. This keeps answers focused and reduces irrelevant context.

### Research and evidence

Ask for claims to be separated from assumptions, sources to be linked, and unknowns to be listed. Preserve source dates and uncertainty. For changing or consequential facts, ask the assistant to verify current primary sources.

### Projects and handoffs

For complex work, ask for a plan before implementation. Keep the plan, decisions, and next action on the project page. At the end of a session, ask for a handoff so the next session can resume without rereading everything.

### Multiple AI clients

Codex and Claude can use the same Markdown vault. Open the same installed folder in either client. Their client settings and sign-ins are separate; the notes are shared. Do not have both agents edit the same files at once. Review changes in Git or your editor when possible.

### External tools and privacy

The vault stores local Markdown, but an AI client may send the context it reads to its provider. Review each provider’s account and privacy settings. Keep passwords, API keys, and recovery codes outside the vault. Connecting a tool requires separate installation, sign-in, and access checks; instructions in a skill do not mean that the connection is active.

## Troubleshooting

- **The assistant ignores the brain:** confirm the client opened the installed folder containing `AGENTS.md` and `CLAUDE.md`, not the downloaded distribution folder.
- **It cannot find a file:** ask it to list/search the folder, and confirm the note is inside the opened vault.
- **It makes up a fact:** ask for the source, correct the canonical note, and tell it to mark unknowns instead of filling gaps.
- **The vault feels overwhelming:** use only the board, profile, journal, and relevant project page for a week. Leave other folders empty.
- **A tool workflow fails:** check `_system/docs/SETUP.md` for separate setup requirements and copy the exact error for diagnosis.
- **You want a clean start:** install the template into a new empty folder. Never install over a populated vault; the installer refuses to overwrite files.

## A one-week start

**Day 1:** finish onboarding and check your profile. **Day 2:** capture one real task and its next action. **Day 3:** use it to prepare for a meeting or focused work session. **Day 4:** debrief and file the outcome. **Day 5:** ask for a brief and correct anything stale. **Day 6:** try research or planning. **Day 7:** ask what is useful, what is confusing, and simplify the setup.

The goal is not to build a perfect archive. The goal is to spend less time reconstructing context and more time doing the work that matters. A well-used second brain should make the next useful action easier to see.

## Suggested next step

Tell your assistant: “Read this field guide and walk me through the first week. Start by checking whether onboarding is complete, then help me choose one real task to run through the system.”
