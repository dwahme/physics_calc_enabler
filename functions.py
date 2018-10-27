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
