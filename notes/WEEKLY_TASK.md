# Weekly update task

The scheduled task runs this file. Edit it here to change what the weekly
update does; no need to touch the schedule.

Repos (both cloned under ~/Documents/GitHub):
- **miomathlab** (public): the app, the skill, GOALS.md, this file.
- **miomathlab-progress** (private): Mio's data. Weekly inbox, snapshots, and
  the long-term progress report. Never copy her data into the public repo.

## 1. Read the brief

Read `miomathlab/GOALS.md` first. Use the fraction-lab-update skill for how the
app is built, tested, and shipped.

## 2. Gather this week's evidence

- `git pull` in both repos.
- Read everything in `miomathlab-progress/inbox/` (not `inbox/done/`):
  - **Progress code** (starts with `FL1:`): base64 → JSON. Save the decoded JSON
    as `snapshots/<YYYY-MM-DD>.json`. Use `mastery` (stage per skill and recent
    attempts), `days` (daily totals per skill: n, c = right, ind = on her own,
    x = explained, sl = step slips, add = adding mix-up, h = hints),
    `stageLog` (moves up and down the ladder), `history` (latest problems), and
    `levels`.
  - **Worksheet photos:** note the lesson, the skill, and her mistakes.
  - **Deb's notes:** anything she observed.
- If the inbox is empty, use the latest snapshot and say so.

## 3. Update the long-term progress report

Rewrite `miomathlab-progress/PROGRESS.md`, keeping the history sections:
- **Ladder now:** a table with skill, stage, weeks at that stage, and last-10
  right / on her own.
- **Weekly trend:** one row per week, newest first, from all snapshots: days
  practiced, problems, % right, % on her own, adding mix-ups, hints. Add this
  week's row; never delete old rows.
- **Moves:** stage changes since the last report.
- **School check:** what the worksheets showed vs. what the app shows.
- **This week's focus** and why, per GOALS.md priorities.

Commit and push this to miomathlab-progress main (private, data only).
Move processed inbox files to `inbox/done/`.

## 4. Improve the app (public repo)

- Pick the focus using GOALS.md "How the weekly update should decide".
- Build, test (jsdom walkthrough, every problem type, 40 runs each, nothing with
  errors, "undefined", or "NaN"), and regenerate index.html with make_site.py.
- Never change the storage key `fractionlab.v1` or remove saved fields.
- Add an entry at the top of `RELEASES` in `index.html` (version `YYYY.MM.DD`, the
  date and time in Pacific, one or two kid-free plain lines on what changed) so
  the grown-up view shows which version is on the iPad. Run `date` for the time.
  If `sw.js` or icons changed, bump `VERSION` there too.
- If code structure changed, update the skill's architecture.md.
- If the ladder rules need tuning (she's stuck or moving too fast), propose the
  change in the PR. Don't change the rules silently.
- Branch `weekly/<date>`, commit, push, `gh pr create`. NEVER push to main.
- No data about Mio in the public repo or the PR beyond a general description
  (no codes, no photos, no scores).

PR title: `Week of <date>: <one-line focus>`. Body, written for a parent:
- **Where she is:** 2 to 3 bullets on the ladder and trend (general terms).
- **What changed for Mio:** 2 to 4 bullets.
- **Try with her this week:** 1 to 2 suggestions.
- A pointer to PROGRESS.md in the private repo for the details.

## 5. If something blocks you

Still open the PR as a draft explaining the problem. If you can't push, write
the explanation to `miomathlab-progress/NEEDS-DEB.md`.
