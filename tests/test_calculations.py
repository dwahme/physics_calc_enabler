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

def test_weight_0():
        mass = 10

        result = calculations.weight(mass)

        assert result == 98

def test_weight_1():
        mass = 18

        result = calculations.weight(mass)

        assert result == 9.81 * 18

def test_weight_opt_0():
        mass = 10
        grav = 3

        result = calculations.weight(mass, grav_accel=grav)

        assert result == 30

def test_weight_opt_1():
        mass = 18
        grav = 14

        result = calculations.weight(mass, grav_accel=grav)

        assert result == 252

def test_velocity_angular_0():
    theta = 1
    time = 1

    result = calculations.velocity_angular(theta, time)

    assert result == 1

def test_velocity_angular_1():
    theta = 5
    time = 2

    result = calculations.velocity_angular(theta, time)

    assert result == 2.5

    assert result == 0

def test_velocity_angular_2():
    theta = 234.6
    time = 15

    result = calculations.velocity_angular(theta, time)

    assert result == (234.6 / 15)

def test_velocity_angular_error():
    theta = 5
    time = 0

    with pytest.raises(ZeroDivisionError):
        calculations.velocity_angular(theta, time)

def test_force_rotational_0():
    mass = 0
    omega = 0
    radius = 0

    result = calculations.force_rotational(mass, omega, radius)

    assert result == 0

def test_force_rotational_1():
    mass = 3
    omega = 2
    radius = 4

    result = calculations.force_rotational(mass, omega, radius)

    assert result == 48

def test_force_rotational_2():
    mass = 3.2
    omega = 9.6
    radius = .4

    result = calculations.force_rotational(mass, omega, radius)

    assert result == 3.2 * 9.6 * 9.6 * .4
