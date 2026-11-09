import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "hyg-brightest.csv"
HEADER = ["hyg_id", "name", "distance_ly", "ra_hours", "dec_deg",
          "spectral_type", "constellation", "apparent_magnitude"]


def _read():
    with CSV_PATH.open(newline="") as f:
        reader = csv.reader(f)
        return next(reader), list(reader)


def test_header():
    header, _ = _read()
    assert header == HEADER


def test_rows_are_sane():
    _, rows = _read()
    for r in rows:
        assert len(r) == 8, r
        assert r[0].isdigit(), r
        assert r[1], r
        assert float(r[2]) > 0, r
        assert 0 <= float(r[3]) < 24, r
        assert -90 <= float(r[4]) <= 90, r
        float(r[7])


def test_ids_and_names_unique():
    _, rows = _read()
    assert len({r[0] for r in rows}) == len(rows)
    assert len({r[1] for r in rows}) == len(rows)


def test_sorted_brightest_first():
    _, rows = _read()
    mags = [float(r[7]) for r in rows]
    assert mags == sorted(mags)
