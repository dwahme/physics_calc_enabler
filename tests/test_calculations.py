from physics import calculations
import pytest


def test_velocity_0():
    dist = 1
    time = 1

    result = calculations.velocity(dist, time)

    assert result == 1

def test_velocity_1():
    dist = 5
    time = 2

    result = calculations.velocity(dist, time)

    assert result == 2.5

    assert result == 0

def test_velocity_2():
    dist = 234.6
    time = 15

    result = calculations.velocity(dist, time)

    assert result == (234.6 / 15)

def test_velocity_error():
    dist = 5
    time = 0

    with pytest.raises(ZeroDivisionError):
        calculations.velocity(dist, time)

def test_momentum_0():
    mass = 1
    vel = 1

    result = calculations.momentum(mass, vel)

    assert result == 1

def test_momentum_1():
    mass = 5
    vel = 2

    result = calculations.momentum(mass, vel)

    assert result == 10

def test_momentum_2():
    mass = 0
    vel = 12

    result = calculations.momentum(mass, vel)

    assert result == 0

def test_energy_kinetic_0():
    mass = 1
    vel = 1

    result = calculations.energy_kinetic(mass, vel)

    assert result == .5

def test_energy_kinetic_1():
    mass = 5
    vel = 2

    result = calculations.energy_kinetic(mass, vel)

    assert result == 25

def test_energy_kinetic_2():
    mass = 0
    vel = 12

    result = calculations.energy_kinetic(mass, vel)

    assert result == 0