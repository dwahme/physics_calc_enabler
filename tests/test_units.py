from physics.units import UNITS, Dimensional
import pytest

def test_create_Dimensional_0():
    dim = Dimensional(3, UNITS.s)

    assert dim.value == 3
    assert dim.units_num == UNITS.s
    assert dim.units_denom == 1

def test_create_Dimensional_1():
    dim = Dimensional(5, UNITS.s * UNITS.cd)

    assert dim.value == 5
    assert dim.units_num == UNITS.s * UNITS.cd
    assert dim.units_denom == 1

def test_create_Dimensional_2():
    dim = Dimensional(-12, UNITS.s * UNITS.cd / UNITS.kg)

    assert dim.value == -12
    assert dim.units_num == UNITS.s * UNITS.cd
    assert dim.units_denom == UNITS.kg

def test_create_Dimensional_3():
    dim = Dimensional(6.4, UNITS.s * UNITS.cd / (UNITS.kg * UNITS.s * UNITS.s * UNITS.s * UNITS.s))

    assert dim.value == 6.4
    assert dim.units_num == UNITS.cd
    assert dim.units_denom == UNITS.kg * UNITS.s * UNITS.s * UNITS.s

def test_add_0():
    unit = UNITS.m * UNITS.kg / (UNITS.mol * UNITS.mol)

    dim_1 = Dimensional(4, unit)
    dim_2 = Dimensional(5, unit)

    result = dim_1 + dim_2

    assert result.value == 9
    assert result.units_num == 