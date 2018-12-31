'''
A submodule for running calculations for various values
in both theoretical and experiemental physics.
'''

GRAV_EARTH = 9.81

def velocity(distance, time):
    """Calculates the Newtonian velocity of an object

    Args:
        distance (numeric): the total distance traveled
        time (numeric): the total time of travel

    Returns:
        numeric: the velocity of the object
    """
    pass

def momentum(mass, velocity):
    """Calculates the Newtonian momentum of an object

    Args:
        mass (numeric): the mass of the object
        velocity (numeric): the velocity of the object

    Returns:
        numeric: the momentum of the object
    """
    pass

def energy_kinetic(mass, velocity):
    """Calculates the kinetic energy of an object

    Args:
        mass (numeric): the mass of the object
        velocity (numeric): the velocity of the object

    Returns:
        numeric: the kinetic energy of the object
    """
    pass

def weight(mass, grav_accel = GRAV_EARTH):
    """Calculates the weight of an object

    Args:
        mass (numeric): the mass of the object
        grav_accel (numeric, optional): the gravitational acceleration
            of the object. Defaults to Earth's (9.81 m/s^2)

    Returns:
        numeric: the weight of the object
    """
    pass

def velocity_angular(theta, time):
    """Calculates an angular velocity (omega)

    Args:
        theta (numeric): angle of rotation
        time (numeric): the time to traverse theta

    Returns:
        numeric: the angular velocity
    """
    pass

def force_rotational(mass, omega, radius):
    """Calculates the rotational force an object experiences

    Args:
        mass (numeric): the mass of the object
        omega (numeric): the angular frequency of the object
        radius (numeric): the distance from the point of rotation

    Returns:
        numeric: the rotational force on the object
    """
    pass