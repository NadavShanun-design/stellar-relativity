import pytest

from stellar_relativity.catalog import find, load_catalog


def test_catalog_loads_and_is_sorted():
    stars = load_catalog()
    assert len(stars) >= 15
    distances = [s.distance_ly for s in stars]
    assert distances == sorted(distances)


def test_closest_star_is_proxima():
    stars = load_catalog()
    assert stars[0].name == "Proxima Centauri"


def test_find_is_case_insensitive():
    star = find("proxima centauri")
    assert star.name == "Proxima Centauri"
    assert star.distance_ly == pytest.approx(4.2465)


def test_find_partial_match():
    assert find("Barnard").name == "Barnard's Star"


def test_find_unknown_raises():
    with pytest.raises(KeyError):
        find("Betelgeuse")


def test_distance_parsecs():
    star = find("Proxima Centauri")
    # 4.2465 ly / 3.2616 ly-per-pc ~= 1.302 pc.
    assert star.distance_parsecs == pytest.approx(1.302, abs=1e-2)
