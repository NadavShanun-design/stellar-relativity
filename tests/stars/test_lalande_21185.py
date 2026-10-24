import math
from stellar_relativity.catalog import find
from stellar_relativity.geometry import cartesian


def test_consistency():
    s = find('Lalande 21185')
    assert s.distance_ly > 0
    x, y, z = cartesian(s.ra_hours, s.dec_deg, s.distance_ly)
    assert math.isclose(math.sqrt(x*x + y*y + z*z), s.distance_ly, rel_tol=1e-9)
