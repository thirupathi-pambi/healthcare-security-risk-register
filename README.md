# Healthcare Security Risk Register & Remediation Tracker

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A Python tool that scores security findings on a likelihood × impact matrix and summarizes open and mitigated risks by severity and remediation status.

> Built on fabricated findings only. Scoring is illustrative and is not a substitute for a formal HIPAA risk analysis.

## Why this exists

Security and compliance teams need a clear answer to "what are our biggest open risks, who owns them, and what has been fixed?" This project models a simple risk register with a documented scoring method and produces a summary suitable for a governance meeting.

## How it works

- Each finding in `data/risks.csv` has a likelihood and an impact rating on a 1–5 ordinal scale.
- Risk score = likelihood × impact, grouped into severity bands.
- The summary reports counts by severity and by remediation status (open vs. mitigated).
- Model assumptions and limitations are written down in `docs/security-notes.md`.

## Project structure

```
.
├── data/
│   └── risks.csv              # fabricated security findings
├── src/
│   └── main.py                # scoring and aggregate report
├── docs/
│   └── security-notes.md      # model limitations
├── tests/
│   └── test_main.py
├── output/
│   └── risk_summary.json      # generated summary
├── LICENSE
└── README.md
```

## Quick start

Requires Python 3.10+ (standard library only). Run from the repository root.

```bash
python src/main.py                      # writes output/risk_summary.json
python -m unittest discover -s tests
```

## Limitations and next steps

- Ordinal 1–5 scores are a prioritization aid, not a quantitative risk measure.
- No control mapping (for example HIPAA Security Rule safeguards or NIST) or due-date tracking yet.
- Possible extensions: owner and due-date fields with overdue alerts, mapping findings to framework controls, and an HTML heat map of the matrix.

## License

MIT. See [LICENSE](LICENSE).
