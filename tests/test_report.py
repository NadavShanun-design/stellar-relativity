import pytest

from stellar_relativity.report import report, report_lines
from stellar_relativity.catalog import find


def test_report_contains_key_sections():
    text = report("Proxima Centauri", beta=0.9)
    assert "Proxima Centauri" in text
    assert "Lorentz factor" in text
    assert "light-travel time" in text


def test_report_lines_is_list():
    lines = report_lines(find("Sirius A"), beta=0.5)
    assert isinstance(lines, list) and len(lines) > 5


def test_report_unknown_star_raises():
    with pytest.raises(KeyError):
        report("Betelgeuse")
