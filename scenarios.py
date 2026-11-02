"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "I am so proud of the person you are becoming. You bring so much laughter, love, and happiness to our family. Keep being curious, brave, helpful, and kind. I hope you always believe in yourself, enjoy learning new things, and follow your dreams.",
            "I like watermelons. They are my favorite fruit. Too bad they are more expensive in winter. I wish I can eat them all year round.",
            "In many developing countries, people are still struggling to feed their family. Here in the United States, kids are required to throw away unfinished lunch at school. I understand the safety concerns. But is there a better way to reduce waste?",
            "When latternflies and cicidas appear, there seem to be so many of them. They sing during summer. Then weather gets colder, they die off. This reminds me of humans. A person may live into 120s, but cannot live forever. A generation of us come and go at about the same time in the long history of the world. Nothing can last forever.",
            "I wish there is more time everyday. I wish I can split into several copies of myself. One copy is working and making money. One copy is taking care of my family and fulfilling my responsibilities. One copy is just enjoying life.",
            "Dogs or cats? I like both of them, but I cannot keep either as pet at home. They have furs and I hate to vacuum constantly. They also are easy to carry bugs around. I am afraid of getting infested.",
            "I like tea very much. I remember when I was young, my grandma often made a pot of tea, and enjoy it with friends and family. But I do not have a lot of time to enjoy it. How I wish I could have plenty of time everyday to savor the pot of tea I make.",
            "High school swim practices start again at the nearby rec center. The time slots that I often use for my workouts are all booked by the swim teams. It is supposed to last for 3 months. I am in a debate whether to freeze my annual membership during the 3 months, since I only use rec center for swimming.",
            "I recently started learning to play the guitar. It is challenging but also very rewarding. I practice for at least an hour every day, and I can already play a few songs. I hope to improve steadily and maybe even perform in front of friends someday.",
            "Last weekend, I went hiking with my friends in the nearby mountains. The weather was perfect, and the scenery was breathtaking. We took lots of photos and enjoyed a picnic at the summit. It was a refreshing break from our usual routine."
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,
        # Same topic, matched length — one confidently AI-style, one confidently
        # human, so a gap here is about the signals and not about topic or length.
        "texts": [
            "Taking a dog for a walk in the evening offers numerous benefits for "
            "both the pet and the owner. Regular exercise helps maintain a "
            "healthy weight, reduces anxiety, and strengthens the bond between "
            "dog and owner. Additionally, evening walks provide an opportunity "
            "to unwind after a long day, allowing both parties to enjoy fresh "
            "air and a change of scenery. Establishing a consistent routine "
            "further reinforces positive behavior and overall well-being for "
            "the dog.",
            "We went out around eight because the dog wouldn't stop pacing by "
            "the door, and honestly I didn't feel like it after the day I'd "
            "had. Turned out to be fine — cooler out, hardly anyone around, "
            "and he found a tennis ball someone left by the fence that kept "
            "him busy the whole way back. Not the walk I planned but it "
            "worked out.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # Inputs spread across the score range, so all three labels are
        # actually reachable — not just the two ends.
        "texts": [
            "Effective time management is essential for personal and "
            "professional success. By prioritizing tasks, setting clear "
            "goals, and maintaining a consistent schedule, individuals can "
            "significantly improve their productivity. Furthermore, "
            "incorporating short breaks throughout the day helps to sustain "
            "focus and prevent burnout. Ultimately, these strategies, when "
            "applied consistently, lead to meaningful improvements in "
            "overall efficiency and well-being.",
            "I missed my bus twice this week because I kept hitting snooze, "
            "so now I just set my alarm for ten minutes earlier and leave "
            "the phone across the room. It's annoying but it works. "
            "Yesterday I actually made it to the stop early enough to grab "
            "coffee, which hasn't happened since probably March.",
            "The meeting ran long, but we covered everything on the list. "
            "Most people seemed satisfied with the plan, though a couple of "
            "questions are still open for next time.",
        ],
    },
    # Criterion 4 — the appeal path — can't be expressed as "texts" or
    # "bodies": it needs a submission's content_id fed into a second request
    # to /appeal, and this file only drives /submit. Tested by hand instead:
    # submit, take the content_id back, POST /appeal against it, confirm the
    # log shows an "appeal" event with status "under_review".
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
        ],
    },
]



def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
