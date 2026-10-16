---
name: fraction-lab-update
description: >
  Update, extend, and ship Mio's Fraction Lab, the iPad fractions practice app Deb
  built for her daughter Mio (kawaii characters, real-world problems, "Understand
  the problem, break it down, then prove it" steps). Edits the single-file app,
  keeps the Claude artifact and the GitHub Pages site (debamoto/miomathlab) in
  sync, and adds new content: new problem types, real-world scenes, characters,
  steps, or a new math unit. Use this whenever Deb mentions the fraction app,
  Fraction Lab, Mio's math app, or says things like "add a new problem type,"
  "add a scene," "Mio got stuck on…," "change the home page," "ship the fraction
  app," "push the update," "add decimals," or leaves an artifact comment on the
  Fraction Lab, even if she doesn't name the app.
---

# Fraction Lab update workflow

The app is ONE self-contained HTML file. A change is only done when it is live in
both places Mio might open it: the Claude artifact and the GitHub Pages site.

## Key facts

- **Claude artifact**: https://claude.ai/artifact/YTy51GvrZ5pBnGwwDBZpt2
  (same artifact also appears as https://claude.ai/code/artifact/fecf30b4-ba57-460b-8c44-887b1cd6a9cb;
  Deb's comments arrive on that URL)
- **GitHub repo**: https://github.com/debamoto/miomathlab
- **Local folder** (once cloned): `/Users/debkawamoto/Documents/GitHub/miomathlab`
- **Live site**: https://debamoto.github.io/miomathlab/
- **Who it's for**: Mio, 4th grade, Illustrative Mathematics Grade 4 Unit 2
  (equivalent fractions and comparing). Strong visual thinker; reading is hard,
  so everything is read aloud and explanations are taps, numbers, or drawings,
  never long typing. Known mix-up: adds the same number to top and bottom
  (wrote 6/11 for 3/8) and struggles with fractions greater than 1.

## Read the learning brief first

`GOALS.md` at the repo root says what the app is for (independent mastery, not
engagement), how the mastery ladder works, and how to choose what to build.
Every change should move Mio up the ladder. The weekly scheduled update follows
`notes/WEEKLY_TASK.md`, and Mio's data lives only in the private repo
`debamoto/miomathlab-progress`, never in this public repo.

## Two versions of the same file

| | Artifact version | Site version (`index.html`) |
|---|---|---|
| Source of truth | yes, edit this one | generated from the artifact version |
| Extra head tags | none | manifest, apple-touch-icon, theme-color |
| Offline | none | registers `sw.js` |

Never hand-edit the site version. Make changes in the artifact version, then run
`scripts/make_site.py` to produce `index.html`. Read
`references/architecture.md` before any change bigger than wording or color; it
maps where each piece lives (cast, scenes, generators, steps, checking, screens).

## Step 1: Get the current file

`Artifact(action="read", url=<artifact url>)` copies the live file into the
container. Work on that copy. Never retype the whole file from memory.

## Step 2: Make the change

- Small change (wording, color, one rule): `Artifact(action="edit", url, edits)`.
- Bigger change (new problem type, new scene, new screen): edit the copied file
  with a short Python read-modify-write, then publish with `url`.
- Keep the established design decisions (see architecture.md, "Decisions Deb has
  made"). Characters are original designs; never draw known characters.
- New problems must stay real-world (a character doing something), read aloud,
  and broken into checked steps.

## Step 3: Test before shipping

```bash
node --check <extracted script>    # syntax
```
Then drive every problem type in jsdom (`npm i jsdom@24`): start each practice
skill, walk every step (tap choices, fill inputs), answer, press Check, and
confirm feedback renders with no "undefined" or "NaN". Run each type 40 times,
since problems are randomly generated. Fix anything that sticks.

## Step 4: Publish the artifact

`Artifact(action="publish", file_path=<copy>, url=<artifact url>, favicon="🧪",
title="Mio's Fraction Lab")`. If the change answers one of Deb's artifact
comments, reply in that thread and resolve it.

## Step 5: Ship the site

```bash
python3 scripts/make_site.py <artifact file> <output folder>/index.html
```
- If the local repo is mounted: copy `index.html` in, `git add index.html`,
  commit with a message about the effect ("Add farmers-market decimal scenes"),
  then ask Deb to run `cd /Users/debkawamoto/Documents/GitHub/miomathlab && git push origin main`.
- If not mounted: give Deb the new `index.html` (present_files) and the steps:
  repo, Add file, Upload files, drop it in, Commit changes.
- `sw.js`, `manifest.webmanifest`, and `icons/` live at the repo root and rarely
  change. If icons or `sw.js` change, bump `VERSION` in `sw.js` and ship it too.

## Step 6: Verify

After ~2 minutes, `web_fetch` the live site and confirm the specific change is in
the HTML. If Pages hasn't redeployed yet, say so and offer to check again.

## This skill lives in the same repo

The repo is also a plugin marketplace (`.claude-plugin/marketplace.json`), and
this skill is at `plugins/fraction-lab-update/skills/fraction-lab-update/`.
To change the skill itself, edit it there and push, in the same commit as any
app change it describes. Claude on claude.ai and Claude Code pick it up on their
next sync. Don't add a `version` field to `plugin.json` or the marketplace
entry; without one, updates follow each commit.

## Protect Mio's progress

Progress lives in the iPad's browser storage under key `fractionlab.v1`. Never
rename that key or remove fields from the saved state; add new fields with
defaults in `freshState()` so old saves keep loading. If a change could reset
progress, warn Deb first and remind her of "Make a backup code" in the grown-up
view.

## Reporting back

One line per change, then: artifact updated, site push confirmed or pending,
live site confirmed or still deploying. Skip recapping how the app works.
