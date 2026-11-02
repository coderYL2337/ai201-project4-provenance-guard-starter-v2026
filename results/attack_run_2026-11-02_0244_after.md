# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-02 02:44
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `2e09f63d-5022-4ffe-a895-008671843a65` | unsure | 0.466 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `6cef0135-67f5-448b-999b-4a384969553e` | unsure | 0.457 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8ce08f9a-a338-4804-a74c-440e4b45d550` | unsure | 0.521 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ef8be03f-18df-44bd-9d43-97762ebc47ee` | unsure | 0.619 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `4af627d2-c4cb-4918-a9d3-117cf5476f5b` | unsure | 0.429 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `db8e02a5-f9aa-4f90-addd-547e12e015cb` | unsure | 0.536 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `88297179-63fc-4ba9-adac-72f1a14a273f` | unsure | 0.451 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `fb6a97ac-efdf-4c40-bc34-6c35626d9f46` | unsure | 0.441 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4f7f2754-29f8-4e06-a0fd-6c78b56247e7` | unsure | 0.608 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `0ad81b72-6c06-48aa-8322-efa12ae004ab` | ai | 0.828 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `520e7b24-56e6-4610-b2e4-75de1f3c98ff` | unsure | 0.609 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `93606c16-dac9-48a5-be6f-3c457eca6c15` | unsure | 0.684 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `597a1a8e-56f7-4c8c-8989-b4f2115a3653` | unsure | 0.689 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `735edd8b-89bd-42b3-953c-4d57afb6b417` | unsure | 0.675 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ae9c1a82-f20f-4be7-8ba3-b43073894087` | unsure | 0.726 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `3e7b9e4b-ece8-47fa-b0a1-9707b3f6599e` | unsure | 0.689 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a7ece4c5-153e-40e7-843e-08e643e0b425` | unsure | 0.731 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `90ac84e7-ea4d-46ba-ae3d-74f6ec6601a9` | unsure | 0.446 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `19dbfef2-add8-4953-b866-f323ed85b6a4` | unsure | 0.486 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ae0fb157-c493-4506-bcf5-f8507f4e5b72` | human | 0.325 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `fa7ccae9-e149-44bc-9f11-f03ee9253974` | unsure | 0.460 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `9bc86ebd-94c5-4f72-88cd-e1a9e7e0e721` | unsure | 0.447 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `5195a1e3-36fb-47e6-a866-84dc76975a7c` | unsure | 0.365 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e2999f9d-b900-4387-9cda-de4cf17e59a7` | unsure | 0.590 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `3a4b688f-f2ea-442a-ba1e-22d4fbe35bea` | human | 0.325 |  |
| MF04 | malformed | text is only punctuation | 200 | `8cc1ecf0-bf33-4997-ac82-1a3956ea14b6` | unsure | 0.654 |  |
| MF05 | malformed | text is a very long single word | 200 | `418040ca-aecc-4661-b438-b5953121a193` | unsure | 0.674 |  |
| MF06 | malformed | text is emoji only | 200 | `8866e3ec-f0cc-4f17-bbfc-eae09855af94` | ai | 0.891 |  |
| MF07 | malformed | text is right-to-left script | 200 | `ea79d41e-bcd1-4e5e-a6d6-7bf70d887a67` | ai | 0.859 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `bfd65013-4fbb-4d7c-9b6d-ff860738cf29` | ai | 0.894 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `8aacfa9c-4cda-4412-baaf-d87d9a079804` | unsure | 0.409 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `33b5d72f-5f01-45b2-802e-ff3147579c43` | human | 0.342 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d503bcb2-310e-4ecf-a3a6-775316da8fa8` | human | 0.335 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4a8fea6f-30a4-4ad2-8dce-440058eae787` | human | 0.335 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6395e17a-57ff-4318-8c77-20326d57cd46` | human | 0.335 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `47557401-38de-482e-a7fe-9bdaaa13ec41` | human | 0.335 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7bd60a9d-ac17-4cbb-904b-db9563967b96` | human | 0.335 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `556a0200-4111-490f-9b93-7c9b7eff68b2` | human | 0.335 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a0ea7f9f-7932-4b37-9677-cf00f74284fa` | human | 0.335 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `621434a9-b609-466b-8b9e-0a23242c948d` | human | 0.335 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7ed0a4a1-a53c-4696-873e-a644edbf097d` | human | 0.335 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ee243aa6-fc37-4439-bcb0-9f927b2e6dea` | human | 0.335 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "2e09f63d-5022-4ffe-a895-008671843a65",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.46588000000000007,
  "model_score": 0.1635,
  "style_score": 0.6287,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "6cef0135-67f5-448b-999b-4a384969553e",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.456955,
  "model_score": 0.5943,
  "style_score": 0.383,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "8ce08f9a-a338-4804-a74c-440e4b45d550",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.52112,
  "model_score": 0.6662,
  "style_score": 0.443,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "ef8be03f-18df-44bd-9d43-97762ebc47ee",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.61907,
  "model_score": 0.6114,
  "style_score": 0.6232,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "4af627d2-c4cb-4918-a9d3-117cf5476f5b",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.42896999999999996,
  "model_score": 0.3212,
  "style_score": 0.487,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "db8e02a5-f9aa-4f90-addd-547e12e015cb",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.53552,
  "model_score": 0.5727,
  "style_score": 0.5155,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "88297179-63fc-4ba9-adac-72f1a14a273f",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.451325,
  "model_score": 0.5862,
  "style_score": 0.3787,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "fb6a97ac-efdf-4c40-bc34-6c35626d9f46",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.44085,
  "model_score": 0.2452,
  "style_score": 0.5462,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "4f7f2754-29f8-4e06-a0fd-6c78b56247e7",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.60826,
  "model_score": 0.7042,
  "style_score": 0.5566,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "0ad81b72-6c06-48aa-8322-efa12ae004ab",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.827815,
  "model_score": 0.9792,
  "style_score": 0.7463,
  "label": "We think this was most likely written by AI, not a person.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "520e7b24-56e6-4610-b2e4-75de1f3c98ff",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.6090500000000001,
  "model_score": 0.6175,
  "style_score": 0.6045,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "93606c16-dac9-48a5-be6f-3c457eca6c15",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.68423,
  "model_score": 0.7387,
  "style_score": 0.6549,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "597a1a8e-56f7-4c8c-8989-b4f2115a3653",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.68927,
  "model_score": 0.8051,
  "style_score": 0.6269,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "735edd8b-89bd-42b3-953c-4d57afb6b417",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.674625,
  "model_score": 0.8329,
  "style_score": 0.5894,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "ae9c1a82-f20f-4be7-8ba3-b43073894087",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.726075,
  "model_score": 0.8005,
  "style_score": 0.686,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "3e7b9e4b-ece8-47fa-b0a1-9707b3f6599e",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6890000000000001,
  "model_score": 0.8814,
  "style_score": 0.5854,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "a7ece4c5-153e-40e7-843e-08e643e0b425",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.7307349999999999,
  "model_score": 0.8816,
  "style_score": 0.6495,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "90ac84e7-ea4d-46ba-ae3d-74f6ec6601a9",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.44560500000000003,
  "model_score": 0.3223,
  "style_score": 0.512,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "19dbfef2-add8-4953-b866-f323ed85b6a4",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.48616,
  "model_score": 0.4625,
  "style_score": 0.4989,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "ae0fb157-c493-4506-bcf5-f8507f4e5b72",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.325235,
  "model_score": 0.2044,
  "style_score": 0.3903,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "fa7ccae9-e149-44bc-9f11-f03ee9253974",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.45981500000000003,
  "model_score": 0.5943,
  "style_score": 0.3874,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "9bc86ebd-94c5-4f72-88cd-e1a9e7e0e721",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.44689,
  "model_score": 0.4998,
  "style_score": 0.4184,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "5195a1e3-36fb-47e6-a866-84dc76975a7c",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.36521499999999996,
  "model_score": 0.6401,
  "style_score": 0.2172,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "e2999f9d-b900-4387-9cda-de4cf17e59a7",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.589955,
  "model_score": 0.5583,
  "style_score": 0.607,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "3a4b688f-f2ea-442a-ba1e-22d4fbe35bea",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.325,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "8cc1ecf0-bf33-4997-ac82-1a3956ea14b6",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.6539200000000001,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "418040ca-aecc-4661-b438-b5953121a193",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.67416,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "8866e3ec-f0cc-4f17-bbfc-eae09855af94",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.89056,
  "model_score": 0.9969,
  "style_score": 0.8333,
  "label": "We think this was most likely written by AI, not a person.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "ea79d41e-bcd1-4e5e-a6d6-7bf70d887a67",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.858885,
  "model_score": 0.9064,
  "style_score": 0.8333,
  "label": "We think this was most likely written by AI, not a person.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "bfd65013-4fbb-4d7c-9b6d-ff860738cf29",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8943249999999999,
  "model_score": 0.9876,
  "style_score": 0.8441,
  "label": "We think this was most likely written by AI, not a person.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "8aacfa9c-4cda-4412-baaf-d87d9a079804",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.408825,
  "model_score": 0.2395,
  "style_score": 0.5,
  "label": "We can't tell with confidence whether this was written by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "33b5d72f-5f01-45b2-802e-ff3147579c43",
  "creator_id": {
    "id": "x"
  },
  "guess": "human",
  "confidence": 0.34222,
  "model_score": 0.0492,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 500,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>AttributeError: &#39;list&#39; object has no attribute &#39;get&#39;\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes",
  "verdict": "BROKE"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "d503bcb2-310e-4ecf-a3a6-775316da8fa8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "4a8fea6f-30a4-4ad2-8dce-440058eae787",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "6395e17a-57ff-4318-8c77-20326d57cd46",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "47557401-38de-482e-a7fe-9bdaaa13ec41",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "7bd60a9d-ac17-4cbb-904b-db9563967b96",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "556a0200-4111-490f-9b93-7c9b7eff68b2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "a0ea7f9f-7932-4b37-9677-cf00f74284fa",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "621434a9-b609-466b-8b9e-0a23242c948d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "7ed0a4a1-a53c-4696-873e-a644edbf097d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "ee243aa6-fc37-4439-bcb0-9f927b2e6dea",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.33504500000000004,
  "model_score": 0.0287,
  "style_score": 0.5,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
