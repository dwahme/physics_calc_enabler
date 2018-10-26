import math
import statistics

def get_average(values):

    total = sum(values)
    amount = len(values)

    return total / amount

def calc_uncertainty(values):
    return statistics.stdev(values)

def calc_rotational_force(mass, omega, radius):
    return mass * omega * omega * radius

def calc_rotational_force_uncertainty(mass, omega, radius, d_mass, d_omega, d_radius):
    
    mass_err = omega * omega * radius * d_mass
    omega_err = d_omega * d_omega * radius * mass
    radius_err = omega * omega * d_radius * mass

    error_square_sum = mass_err * mass_err + omega_err * omega_err + radius_err * radius_err
    
    return math.sqrt(error_square_sum)