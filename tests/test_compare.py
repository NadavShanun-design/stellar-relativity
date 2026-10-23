from stellar_relativity.compare import comparison_rows, comparison_table


def test_comparison_rows_cover_catalog():
    rows = comparison_rows(beta=0.9)
    assert len(rows) >= 15
    for r in rows:
        assert r["onboard_trip_years"] < r["earth_trip_years"]
        assert r["years_saved"] > 0


def test_comparison_table_is_text():
    table = comparison_table(beta=0.5)
    assert "Proxima Centauri" in table
    assert "Onboard" in table
