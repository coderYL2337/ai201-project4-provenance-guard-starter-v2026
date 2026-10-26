# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A `POST /submit` arrives with `{"text": ..., "creator_id": ...}`.
2. The route checks `text` is a non-empty string — bad input gets a `400`
   immediately, before any model runs.
3. `detector.model_signal(text)` runs GPT-2 locally, measures how predictable
   the text is (perplexity), and turns that into a 0–1 `model_score`.
4. `stylometry.style_signal(text)` measures sentence-length variation,
   vocabulary variety, and punctuation density, and turns those into a 0–1
   `style_score` — same direction as the model signal, higher means more
   likely AI.
5. `scoring.combine_signals(model_score, style_score)` merges the two into
   one 0–1 score, weighted 0.35/0.65 toward the style signal.
6. `scoring.score_to_label(combined_score)` turns that number into a
   machine-readable `guess` and the exact sentence a reader sees.
7. `audit.log_decision(...)` writes one JSON line to `logs/audit.jsonl` with
   both signal scores, the combined score, and the label; the route answers
   with `content_id`, `guess`, `confidence`, `label`, `model_score`, and
   `style_score`.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:**

### Signal two — the style signal

**What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:**

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** a weighted average, weighted toward the style signal rather
than split evenly. The model signal's failure mode is structural — it reads
plain, ordinary human writing as AI-like, with nothing the writer did wrong.
The style signal's failure mode requires someone to deliberately reshape
their sentences. When the two disagree, I'd rather the result lean on the
harder-to-trigger failure — which in practice means leaning toward whichever
signal reads lower, since it's the model signal that tends to run high on
honest writing.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.35`, `WEIGHT_STYLE_SIGNAL = 0.65`
(`config.py`).

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

Three calibration texts through both signals (`model_score` / `style_score`):

| Text | model_score | style_score |
|---|---|---|
| Clearly AI (generic framework paragraph) | 0.8864 | 0.6361 |
| Clearly human (toast/keys anecdote) | 0.6846 | 0.5852 |
| Borderline (plain "went to the store" diary) | 0.8591 | 0.6239 |

They **agree on ranking** — both put the AI paragraph highest and the human
anecdote lowest — but **split on confidence** for the clearly-AI text: `model_score`
clears `AI_THRESHOLD` (0.65) on its own, `style_score` stays just under it, in
the unsure band. The split that worries me more is the clearly-human text:
`model_score` (0.6846) alone would call a true human anecdote "high-confidence
AI" just for using short sentences and common words — the exact blind spot
named in `detector.py`. `style_score` (0.5852) pulls the other way, so a
simple average lands at 0.635, just under the AI threshold — "unsure" rather
than an outright wrong accusation. That's the case `combine_signals` has to
handle: when the model signal is ready to accuse plain writing, the style
signal needs enough weight to drag it back out of the AI band, not just
average it into "unsure" by luck.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | "We think this was probably written by a person." |
| unsure | 0.35 – 0.65 | "We can't tell with confidence whether this was written by a person or by AI." |
| high-confidence AI | 0.65 – 1.00 | "We think this was most likely written by AI, not a person." |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

It names the actual situation — the system couldn't decide — instead of picking
a side and hedging with a number. It doesn't say "flagged" or "suspicious,"
because someone who wrote every word themselves could land here just as
easily as someone who didn't, and nothing in the wording should make the
honest writer feel accused for being hard to read.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I burned the toast again this morning, swore at it, and ate it anyway because I was already late. My neighbors dog barked the whole time I was trying to find my keys -- which, of course, were sitting right on top of the fridge where Id left them last night.", "creator_id": "lucy_appeal_demo"}'
```

```json
{
  "confidence": 0.55888,
  "content_id": "0928c761-8336-40f4-9e81-1b863c19a130",
  "guess": "unsure",
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "model_score": 0.51,
  "style_score": 0.5852
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "0928c761-8336-40f4-9e81-1b863c19a130", "reasoning": "I wrote this myself this morning, it is a true story about my own breakfast."}'
```

```json
{
  "content_id": "0928c761-8336-40f4-9e81-1b863c19a130",
  "message": "Appeal recorded. A human will review this decision.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.55888,
      "content_id": "2ebe7218-c8cc-4fbc-8f7a-78609f5faa87",
      "creator_id": "calib_unsure2",
      "guess": "unsure",
      "label": "We can't tell with confidence whether this was written by a person or by AI.",
      "model_score": 0.51,
      "status": "decided",
      "style_score": 0.5852,
      "timestamp": "2026-10-26T06:27:04+00:00"
    },
    {
      "combined_score": 0.55888,
      "content_id": "0928c761-8336-40f4-9e81-1b863c19a130",
      "creator_id": "lucy_appeal_demo",
      "guess": "unsure",
      "label": "We can't tell with confidence whether this was written by a person or by AI.",
      "model_score": 0.51,
      "status": "decided",
      "style_score": 0.5852,
      "timestamp": "2026-10-26T06:28:58+00:00"
    },
    {
      "content_id": "0928c761-8336-40f4-9e81-1b863c19a130",
      "creator_id": "lucy_appeal_demo",
      "event": "appeal",
      "reasoning": "I wrote this myself this morning, it is a true story about my own breakfast.",
      "status": "under_review",
      "timestamp": "2026-10-26T06:29:06+00:00"
    }
  ]
}
```

---


## How I Used AI

**Moment 1**

- *What I asked for:* Help after `python detector.py "..."` crashed with a
  NumPy ABI error (`numpy.dtype size changed... Expected X from C header, got
  Y`) right after setting up the venv.
- *What came back:* An explanation that the installed torch build was compiled
  against NumPy 1.x's C ABI, so an unconstrained install had pulled in NumPy
  2.x, plus the fix: pin `numpy<2.0`.
- *What I changed:* Added an explicit `numpy<2.0` line to `requirements.txt`
  (it had been an unpinned transitive dependency of torch/transformers) and
  reinstalled.

**Moment 2**

- *What I asked for:* Run both signals over four calibration texts (clearly
  AI, clearly human, formal human, lightly-edited AI) and investigate if any
  score looked surprising.
- *What came back:* `formal_human` — a single long, semicolon-joined human
  sentence — scored almost as AI-like as the lightly-edited AI text. Printing
  the three raw stylometry measures separately showed `sentence_length_spread`
  returning `0.0` for a one-sentence input, which `style_signal` was reading
  as "maximally uniform, therefore AI-like" instead of "not enough sentences
  to measure."
- *What I changed:* In `stylometry.py::style_signal`, a sentence count under 2
  now scores that component as a neutral 0.5 instead of 1.0, so missing
  evidence no longer reads as strong evidence of AI.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
