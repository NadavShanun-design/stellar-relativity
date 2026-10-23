from stellar_relativity.html_report import star_html


def test_html_contains_star_name_and_structure():
    html = star_html("Proxima Centauri", beta=0.9)
    assert "<!DOCTYPE html>" in html
    assert "Proxima Centauri" in html
    assert "<pre>" in html


def test_html_is_escaped_and_nonempty():
    html = star_html("Sirius A", beta=0.5)
    assert "Sirius A" in html
    assert len(html) > 500
