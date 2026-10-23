from stellar_relativity.starmap import ascii_sky


def test_ascii_sky_dimensions():
    art = ascii_sky(width=72, height=22)
    lines = art.splitlines()
    # header + top ruler + 22 rows + bottom ruler + caption
    assert len(lines) == 22 + 4
    assert "*" in art


def test_ascii_sky_rejects_tiny_grids():
    import pytest

    with pytest.raises(ValueError):
        ascii_sky(width=5, height=5)
