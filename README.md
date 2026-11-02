# Healthcare Security Risk Register & Remediation Tracker

> **Portfolio demonstration | Synthetic / fictional data only**

Models security risk ownership and mitigation status for fictional healthcare IT assets, with an illustrative likelihood × impact model.

## What this demonstrates
- Track open and mitigated security findings
- Score risks on a documented 1–5 ordinal matrix
- Export summary by severity and remediation status

## Quick start
```bash
python src/main.py
python -m unittest discover -s tests
```

Python 3.10+ is recommended. Core functionality uses the Python standard library; no API keys or patient records are required. Run commands from the repository root.

## Repository contents
- `data/risks.csv`: fabricated security findings
- `src/main.py`: scoring and aggregate report
- `docs/security-notes.md`: model limitations

## Relevant skills
Security governance, HIPAA-aware operations, risk register, Python, compliance reporting

## Data and privacy
All records, facilities, identifiers, events and organizations in this repository are fabricated for demonstrations. This is **not** a production clinical system and does not contain real protected health information (PHI). Do not upload real patient data or confidential employer files. Outputs do not substitute for clinical, privacy, security, or regulatory review.

## How to discuss in an interview
Explain the input, validations or transformations, measurable outputs, tests, and what you would change for a real deployment (authentication, audit logs, monitoring, regulatory review, and secure storage). Describe this as a **personal portfolio project**, not as an implementation at an employer.

## License
MIT — see [LICENSE](LICENSE).
