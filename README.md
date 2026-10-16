# Mio's Fraction Lab

A fractions practice app for iPad, hosted with GitHub Pages. Progress is saved on the device only.

## The app
- `index.html` is the whole app (generated from the Claude artifact version).
- `manifest.webmanifest` and `icons/` let it install to the Home Screen.
- `sw.js` lets it work offline.

## The update skill
This repo is also a Claude plugin marketplace, so the instructions for updating the app live next to the app.
- `.claude-plugin/marketplace.json` lists the plugin.
- `plugins/fraction-lab-update/` is the plugin, with the skill in `skills/fraction-lab-update/`.

Install in Claude Code:

    /plugin install fraction-lab-update --marketplace debamoto/miomathlab

Edit the skill here and push. Claude and Claude Code pick up the change on their next sync.
