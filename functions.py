import math
import statistics

def get_average(values):
    total = sum(values)
    amount = len(values)

    return total / amount

def calc_uncertainty(values):
    return statistics.stdev(values)

def percent_diff(expected, actual):
    return (expected - actual) / expected

def calc_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def calc_omega(time):
    return 2 * math.pi / time

def calc_omega_uncertainty(time, time_d):
    omega_min = 2 * math.pi / (time + time_d)
    omega_max = 2 * math.pi / (time - time_d)

    return get_average([omega_min, omega_max])

def calc_weight(mass):
    return 9.8 * mass

def calc_rotational_force(mass, omega, radius):
    return mass * omega * omega * radius

def calc_rotational_force_uncertainty(mass, omega, radius, d_mass, d_omega, d_radius):

    mass_err = omega * omega * radius * d_mass
    omega_err = 2 * d_omega * omega * radius * mass
    radius_err = omega * omega * d_radius * mass

    error_square_sum = mass_err * mass_err + omega_err * omega_err + radius_err * radius_err

    return math.sqrt(error_square_sum)

def pretty_print_tables(values):
    print("*===========*")
    print("|trial|value|")
    print("|-----------|")
    for i in range(len(values)):
        print(center_line(" trial", i) + "|" + center_line("value ", values[i]))
    print("|===========|")
def center_line(col, val):
    b_num = int(len(col)/2)
    e_num = len(col) - len(str(val)) - b_num
    return (" " * b_num) + str(val) + (" " * e_num)
