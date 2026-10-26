# Timeline — project instructions

## Project

Time-awareness tool for ADHD time-blindness.

**Core philosophy:** Time awareness as liberation, not constraint. This is not meant to be a productivity "maxxing" / grind-mindset app. The goal is to help people understand their time better so they can feel like they have more freedom. Make time *felt*, not just scheduled.

**Stack:** Python backend, SQLite storage, PythonAnywhere hosting, web UI (phone home-screen shortcut), ntfy.sh for push notifications.

**Data model** (`src/event_class.py`):
- `Event` (base) — name, date, topic
  - `AllDayEvent` — type marker only
  - `TimedEvent` — adds time, duration, location
  - `Deadline` — adds time (no duration, no location)

**Core features:**
1. Event intake via phone-friendly web form (filterable by date, topic, name via SQLite)
2. Reverse-scheduled push notifications — works backwards from a deadline, nudges at each step
3. Experience-sampling (ESM) prompts at random intervals, logged to SQLite for self-pattern analysis

## Git conventions

**Commit messages**
- Use imperative mood: `Add Deadline subclass to Event hierarchy`, not `added deadline` or `adding deadline`.
- Be specific about *what* changed: `Fix off-by-one in reverse-schedule offset calculation` beats `fix bug`.
- One logical change per commit. If the message needs the word "and," it's probably two commits.
- Never: `wip`, `update`, `fix`, `asdf`, `final`, `stuff`.

**Branching**
- Work on feature branches, even solo. Branch names: `feature/event-intake-form`, `fix/notification-offset`.
- Merge into `main` via PR (even solo PRs — shows the workflow).
- Delete the branch after merging.

**Pulling**
- `pull.rebase` is set globally (`git config --global pull.rebase true`). Keeps history linear, avoids noisy merge commits.
- Resolve conflicts locally, test, then push.

**Before every commit**
- Review the diff: `git diff --staged`. No stray debug prints, no commented-out code, no secrets.
- Prefer `git add <specific-files>` over `git add .` so you don't accidentally stage junk.

**Never commit**
- `.env` files or anything with API keys, tokens, passwords
- `.db` / `.sqlite` database files (data is local, not source)
- `__pycache__/`, `.venv/`, IDE folders

**README stays current.** When a feature lands, update the README in the same PR.

## File layout (planned)

timeline-adhd/
├── src/
│   ├── event_class.py       # Event data model
│   ├── esm.py               # Experience-sampling response schema + queries
│   ├── db.py                # SQLite setup + shared queries
│   ├── app.py               # Web backend
│   └── notifications.py     # Reverse-scheduling + ntfy integration
├── templates/               # HTML for the web form
├── static/                  # CSS, JS, icons
├── data/                    # SQLite DBs (gitignored)
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
