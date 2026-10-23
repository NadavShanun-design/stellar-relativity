# Contributing

Thanks for your interest in stellar-relativity!

## Principles

- **The physics stays transparent.** Implement formulas from first principles
  with a comment or docstring pointing at the relationship. No magic numbers in
  the physics — only the measured values in `data/stars.json`.
- **One feature per pull request.** Small, reviewable changes.
- **Tests travel with code.** Every physics module has a matching test in
  `tests/`.

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e . && pip install pytest
pytest -q
```

## Adding a star

Append an entry to `data/stars.json` with a real, cited measurement (distance,
RA, Dec, spectral type). The loader and comparison tools pick it up automatically.

## Submitting

1. Fork and branch (`feat/short-description`).
2. Add code + tests; make sure `pytest` is green.
3. Open a PR describing the relationship you added and your source.
