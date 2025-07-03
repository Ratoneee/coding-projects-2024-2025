import pytest
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
    kpa_to_psi
)

def test_water_column_height():
    assert water_column_height(10, 5) == pytest.approx(12.5, abs=0.001)
    assert water_column_height(0, 10) == pytest.approx(5, abs=0.001)
    assert water_column_height(5, 0) == pytest.approx(5, abs=0.001)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(10) == pytest.approx(98.0665, abs=0.001)
    assert pressure_gain_from_water_height(0) == pytest.approx(0, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(30, 0.048692, 1.65, 0.02) == pytest.approx(-9.64, abs=0.01)
    assert pressure_loss_from_pipe(50, 0.048692, 1.75, 0.02) == pytest.approx(-17.17, abs=0.01)

def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == pytest.approx(-0.109, abs=0.001)

def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == pytest.approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == pytest.approx(80069, abs=1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == pytest.approx(-163.744, abs=0.001)

def test_kpa_to_psi():
    assert kpa_to_psi(0) == pytest.approx(0, abs=0.001)
    assert kpa_to_psi(158.7) == pytest.approx(23.02, abs=0.01)
    assert kpa_to_psi(100) == pytest.approx(14.50, abs=0.01)
