# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives on my own writing

<!-- Your criterion. It must name a number. -->

Of 10 short paragraphs I write myself (not AI, not copied from anywhere), at
most 1 is labelled "high-confidence AI" across all three trials.

**Why this target:**

A false accusation costs a real writer a lot — their post gets pulled, their
account looks suspicious, and they have to appeal something they know is
true. Missing some AI text costs the site very little by comparison: a little
more unflagged AI writing in the feed. Because the two mistakes aren't
equally expensive, I'm willing to tolerate a worse miss rate on AI text in
exchange for a much better false-positive rate on human text. 1 in 10 is
strict enough to notice if the detector drifts, but not so strict that any
single unlucky perplexity reading fails the whole criterion.

---

## 2. Score spread between obvious cases

<!-- Your criterion. -->

For a piece of text I'm confident is AI-generated and a piece I'm confident is
human-written on the same topic and length, the combined scores differ by at
least 0.4, in all three trials.

**Why this target:**

If the two signals can't separate the easiest possible case — something
obviously machine-written next to something obviously not — then the
thresholds in `config.py` are arbitrary lines through noise rather than a
meaningful split. 0.4 is roughly the width of two label bands, so a real gap
between clear cases should visibly cross at least one threshold. Requiring it
to hold on all three trials (not just on average) matters because the model
signal runs an actual model, and a spread that only shows up sometimes isn't
something I can rely on to drive a label a reader sees.

---

## 3. All three labels are reachable

<!-- Your criterion. -->

Each of the three labels ("high-confidence human", "unsure", "high-confidence
AI") is produced by at least one submission in every trial, when I submit one
clearly-AI, one clearly-human, and one deliberately borderline text.

**Why this target:**

A label nobody can ever reach isn't a label, it's dead code — and the
config.py warning about a stub style signal collapsing the reachable range is
a real failure mode here, not a hypothetical one. If "high-confidence human"
never fires, every writer effectively starts from "unsure" no matter how
plainly they wrote, which quietly defeats the whole point of having three
bands instead of a single accusation. Checking this on every trial, not just
once, catches the case where a label is reachable in principle but only for a
sliver of scores the model signal rarely lands on.

---

## 4. The appeal path always works

<!-- Your criterion. -->

For 10 separate submissions followed by an appeal against each, 10 out of 10
appeals move the content's status to "under_review" and 10 out of 10 appear
in the audit log, in every trial.

**Why this target:**

The appeal route is the only thing standing between a wrong label and a
writer having no recourse at all, so it has to work every single time — a
9-in-10 success rate here means roughly one in ten wrongly-accused writers
files an appeal that silently does nothing, which is worse than not offering
appeals at all because it looks like due process without providing any. This
is also the one criterion where I don't think any failure rate above zero is
acceptable, since the whole feature exists specifically to catch the mistakes
the detector makes.

---

## 5. Bad input never crashes the service

<!-- Your criterion. -->

Sending `text` missing, `text` as an empty string, `text` as `null`, and
`text` as a 50,000-word string each gets a 4xx JSON response (never a 5xx or
a connection drop), in all three trials, for all four inputs.

**Why this target:**

A submission form on a real site gets malformed input constantly — empty
pastes, JS bugs that send `null`, someone pasting an entire document — and
none of that is an attack, it's just normal use. A crash on any of these turns
a bad paste into a down service for every other writer trying to submit at
the same time, which is a much bigger failure than politely rejecting one bad
request. Requiring a 4xx specifically (not just "didn't crash") means the
service also has to tell the caller what was wrong with their request rather
than failing in a way that looks like a broken endpoint.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
