# Fraction Lab architecture

Everything is in one HTML file: CSS in `<style>`, all logic in one `<script>`
IIFE. Sections are marked with `/* ---------- name ---------- */` comments, in
this order:

| Section | What lives there |
|---|---|
| top of script | `SKILLS` (skill names), `MISSION` (the 6 problem types in a mission, in order), `STRAT_NAMES` (labels for strategies in the grown-up view) |
| kawaii cast | `face()`, `extras()`, `CAST` (each friend: name, unlock star cost `at`, hello `line`, `draw(mood)` SVG), `ch(id,mood)`, `CHEERS`, `ARROW`/`CHECKI` sign icons |
| state | `freshState()`, `load()`, `save()`; storage key `fractionlab.v1` |
| math helpers | fraction helpers, `spoken(f)` for read-aloud, `fr(f)` fraction HTML, input builders |
| speech | read-aloud with voice ranking (Premium/Enhanced first), sentence chunking for iPad Safari |
| generators | `genCompare`, `genBenchmark`, `genMissing`, `genEquiv`, `genFindTwo`, `genStory`; each takes level 1 to 3; `GEN` map |
| real-world scenes | `CTX` (pizza, chocolate, trail, bottle, ribbon, dollar), `pickCtx`, `pickActors`, `dress(P)` attaches scene + characters, `scene()` story text, `card()`, `rowsFor()` |
| visuals | `model()` chooses the picture per scene: `pies`, `lines` (trail number line), `cups` (bottles), `grids` (dollar), `bars`; `commonProof` |
| session | `guideLine`, `setGuide`, `askHTML`, `sayPrompt`, `hintHTML`, `answered`, `updateGo`, `renderProblem`, `onGo` |
| step-by-step coach | `buildSteps()` returns the "Break it down" steps per type; `renderSteps()` is the step engine |
| explain | used only when step-by-step is off: `strategiesFor`, `workHTML`, `showExplain`, drawing pad |
| checking | `evaluateAnswer` (feedback + proof), `evaluateExplain`, `adapt` (difficulty levels 1 to 3), `summary`, `check` (stars, challenge bonus, records mastery) |
| mastery ladder | `STAGES`, `mst(skill)`, `scaffoldFor(skill)` (full / plan / none), `recordMastery` (promotion and demotion rules), `rollup` (daily totals in `S.days`, kept forever), `planMission` (focus skills, due reviews, challenge when ≥90%), `seedMastery` (one-time replay of old history) |
| screens | `renderHome`, `renderEnd`, `renderGrown` (grown-up view: stats, backup code, voice, settings) |

## Saved state (`fractionlab.v1`)

`levels`, `runs` (difficulty), `history` (latest 60 problems, detailed),
`mastery[skill] = {stage, recent[], since, reviewDue}`, `days[YYYY-MM-DD][skill]
= {n, c, ind, x, sl, add, h}`, `stageLog[]`, `stepMode` ('auto' | 'always' |
'off'), stars, friends, streak, voice settings. The grown-up view's "Copy
progress code" exports all of it except drawings as `FL1:` + base64 JSON.

## Problem object `P`

Built by a generator, then `dress(P)` adds `ctxKey`, `ctx`, `who`, `names`; `renderProblem` adds `level`, `challenge`, `review`, `scaffold`. Common fields: `type`, `skill`, `level`, and per type:
compare `a,b,answer(> < =)`; benchmark `a,t,answer`; missing
`left,right,missing,answer`; equiv `base,opts[{f,ok,tag}]`; findtwo `base`;
story `fs,ask,answer(index string)`.

## Recipes

**New real-world scene**: add an entry to `CTX` with `emoji, model, dens,
verb, base, of, obj, more, most, least, half, whole, set` (plus `cut:true,
pieces` if it can be cut into pieces for missing-number problems). `dens` is
the list of denominators the picture can draw. `model` is one of pie, line,
cup, grid, bar.

**New character**: add to `CAST` with an unlock `at` higher than the last one,
a short spoken `line`, and a `draw:m=>` SVG in the 120×120 viewBox using
`face(cx,cy,m,scale)` and the shared outline `O`. Keep it original and kawaii.
Preview it by rendering `ch(id,mood)` for normal, happy, cheer, think.

**New problem type** touches: `SKILLS`, maybe `MISSION`, a `genX` + `GEN`,
`dress` (characters needed), `scene`, `askHTML`, `answered`, `hintHTML`,
`rowsFor`, `guideLine`, `buildSteps`, `evaluateAnswer`, `summary`,
`strategiesFor`, `freshState().levels`. Add a field default rather than
changing old ones.

**New math unit** (for example IM Grade 4 Unit 3, adding and subtracting
fractions, or Unit 5, decimals): treat as new problem types plus their own
mission list; consider a mission picker on the home screen.

## Decisions Deb has made (keep these)

- Motto: "Understand the problem. Break it down. Then prove it."
- Every problem is a real-world scene acted out by the characters, not abstract.
- Kawaii original characters (Mochi, Kelp, Bolt, Hazel, Rio, Dart), unlocked by
  total stars; they react to her answers.
- Step-by-step "Break it down" fades per skill with the mastery ladder (GOALS.md); each step checked with a nudge.
- Mission trail uses green freeway-sign mile markers with a muted mint arrow
  (#5fbf8f) and white number; cleared signs get a white check and gold ring.
- Home page fits one iPad screen (two columns); other pages may scroll.
- Short joyful load animation on home only; respects Reduce Motion.
- Uses Deb's dark-first design system: bg #141312, ink #f2efe9, muted #a8a29a,
  orange #f0a457, teal #3fbdbd, purple #c98ab8, red #ff7a8f; DM Sans with
  Cormorant Garamond for the title.
