"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """
    Combine two 0–1 signals into one 0–1 score.

    Both inputs point the same way: higher means more likely AI. Your output
    should too.

    Args:
        model_score: from `detector.model_signal` — how predictable the text is.
        style_score: from `stylometry.style_signal` — the shape of the text.

    Returns:
        A float from 0.0 (confidently human) to 1.0 (confidently AI).

    **The rule:** a weighted average, weighted toward the style signal
    (`config.WEIGHT_STYLE_SIGNAL` = 0.65 vs `config.WEIGHT_MODEL_SIGNAL` =
    0.35) rather than split evenly. The model signal's failure mode is
    structural — it reads plain, ordinary human writing as AI-like, with
    nothing the writer did wrong. The style signal's failure mode requires
    someone to deliberately reshape their sentences. Leaning on the
    harder-to-trigger failure means that when the two disagree, the result
    sits closer to whichever is lower — which is closer to "human" more often
    than not, since it's the model signal that tends to run high on honest
    writing.

    **The split case this handles** (see README, "A case where my two signals
    split"): a plainly-written human anecdote scored model_score=0.6846 (on
    its own, past `AI_THRESHOLD`) and style_score=0.5852. A 50/50 average
    (0.635) only narrowly avoided an outright false accusation. This rule
    gives 0.6846*0.35 + 0.5852*0.65 = 0.6200 — further from `AI_THRESHOLD`,
    deliberately rather than by luck.
    """
    return (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    )


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.
    ← TODO (Milestone 5)

    Returns:
        (guess, label_text) — where `guess` is a short machine-readable string
        like "ai" / "human" / "unsure", and `label_text` is the full sentence
        shown to a person.

    ⚠️ Write the label text for someone who has never heard the word
    "threshold".

        ✗ "human, 0.81 confidence"
        ✓ "We think this was probably written by a person."

    All three labels have to be **reachable**. If no score can produce one of
    them, your ranges have a gap — and Milestone 5 asks you to submit text that
    produces each one, which is how you'd find out.

    The hardest one to write is "unsure". It has to admit uncertainty without
    sounding like an accusation, because the person reading it may well have
    written every word themselves. Your breakout asks your group what they'd
    think if they got it on their own work. That question is the whole
    milestone.
    """
    if score >= config.AI_THRESHOLD:
        return "ai", "We think this was most likely written by AI, not a person."
    if score <= config.HUMAN_THRESHOLD:
        return "human", "We think this was probably written by a person."
    return "unsure", (
        "We can't tell with confidence whether this was written by a person "
        "or by AI."
    )


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
