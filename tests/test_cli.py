import pytest

from stellar_relativity.cli import main


def test_list_runs(capsys):
    assert main(["list"]) == 0
    assert "Proxima Centauri" in capsys.readouterr().out


def test_report_runs(capsys):
    assert main(["report", "Proxima Centauri", "--speed", "0.9"]) == 0
    assert "Lorentz factor" in capsys.readouterr().out


def test_rocket_runs(capsys):
    assert main(["rocket", "Sirius A", "--g", "1.0"]) == 0
    assert "ship time" in capsys.readouterr().out


def test_map_runs(capsys):
    assert main(["map"]) == 0
    assert "*" in capsys.readouterr().out


def test_unknown_star_exits_nonzero(capsys):
    assert main(["report", "Betelgeuse"]) == 1


def test_bad_speed_exits_nonzero():
    assert main(["report", "Proxima Centauri", "--speed", "1.5"]) == 2
