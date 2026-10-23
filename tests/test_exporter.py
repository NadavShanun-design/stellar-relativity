import json

from stellar_relativity.exporter import export_catalog, export_json, star_payload
from stellar_relativity.catalog import find


def test_star_payload_shape():
    payload = star_payload(find("Proxima Centauri"), beta=0.9, observation_year=2026)
    assert payload["name"] == "Proxima Centauri"
    assert "position_ly" in payload and {"x", "y", "z"} <= payload["position_ly"].keys()
    assert payload["travel"]["proper_time_years"] < payload["travel"]["earth_time_years"]


def test_export_catalog_has_all_stars():
    cat = export_catalog(beta=0.5)
    assert cat["beta"] == 0.5
    assert len(cat["stars"]) >= 15


def test_export_json_is_valid_json():
    parsed = json.loads(export_json(beta=0.9))
    assert parsed["beta"] == 0.9
    assert isinstance(parsed["stars"], list)
