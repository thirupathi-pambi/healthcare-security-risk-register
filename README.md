# Healthcare Security Risk Register

This is a risk register I built for a pretend clinic's security program. I wanted something that could answer the questions that always come up in a security or compliance meeting: what are our biggest open risks, who owns them, and what have we actually fixed?

All the findings are made up. Nothing here comes from a real organization, and this isn't a HIPAA risk analysis.

## How the scoring works

Each finding in `data/risks.csv` gets two ratings from 1 to 5:

- **Likelihood**: how likely it is to happen
- **Impact**: how bad it would be if it did

The score is likelihood × impact, which puts it somewhere from 1 to 25. I split that range into three bands:

| Score | Severity |
|-------|----------|
| 15–25 | High     |
| 7–14  | Medium   |
| 1–6   | Low      |

`src/main.py` scores every finding, counts them by severity and status, and lists the high risks that haven't been closed yet. The result prints to the screen and is saved to `output/risk_summary.json`.

## Running it

You need Python 3.10 or newer. There's nothing to install.

```bash
python src/main.py
python -m unittest discover -s tests
```

Run both commands from the repo root.

## Current register

| ID   | Area     | Finding                              | L × I  | Severity | Status      | Owner               |
|------|----------|--------------------------------------|--------|----------|-------------|---------------------|
| R001 | Identity | Inactive accounts need review        | 4×4=16 | High     | Open        | IT Admin            |
| R002 | Endpoint | Encryption evidence missing          | 3×5=15 | High     | In progress | Security Analyst    |
| R004 | Backup   | Restore testing overdue              | 3×5=15 | High     | Open        | Infrastructure Lead |
| R005 | Network  | Guest network segmentation unchecked | 3×4=12 | Medium   | In progress | Network Engineer    |
| R003 | Training | Annual phishing refresher due        | 2×3=6  | Low      | Mitigated   | Training Lead       |

Three high risks are still open: **R001, R002 and R004**. The backup one stands out to me. If nobody has tested restoring from backups, you don't know whether you could recover from ransomware.

## Some decisions I made

- **"In progress" still counts as open.** A risk only drops off the open list once it's marked `mitigated`. That's why R002 is on the list even though someone is working on it. Being worked on isn't the same as being fixed.
- **Bad scores are rejected.** If a likelihood or impact rating is outside 1–5, like a 0 or a 6, the script raises an error. I'd rather it stop than quietly produce a wrong score. One of the unit tests checks this.
- **Owners are roles, not names.** Using roles keeps the data generic, and it's also closer to how a register should work. When people leave, the risk shouldn't lose its owner.
- **I kept the scoring simple on purpose.** A 1–5 × 1–5 matrix is a way to decide what to fix first. It doesn't measure risk precisely, and I wrote the limits down in `docs/security-notes.md`.

## Files

```
data/risks.csv            security findings with ratings, status and owner
src/main.py               scoring and summary report
docs/security-notes.md    scoring method and its limits
tests/test_main.py        unit tests for scoring and input checks
output/risk_summary.json  generated summary
```

## What I'd add next

- Due dates on each finding, so the report can flag overdue items
- Open high risks grouped by owner role. The `owner_role` column is already in the data, but the summary doesn't use it yet.
- Mapping each finding to a HIPAA Security Rule safeguard or a NIST control
- A small HTML heat map of the likelihood × impact grid
