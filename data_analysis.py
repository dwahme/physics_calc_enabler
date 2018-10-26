import functions

# Add data here
mass_values = [
    0, 0
]
omega_values = [
    0, 0
]
radius_values = [
    0, 0
]

# Calculate averages
mass_ave = functions.get_average(mass_values)
omega_ave = functions.get_average(omega_values)
radius_ave = functions.get_average(radius_values)

# Calculate uncertainties
mass_d = functions.calc_uncertainty(mass_values)
omega_d = functions.calc_uncertainty(omega_values)
radius_d = functions.calc_uncertainty(radius_values)

# Run full rotational calculations
rot_force = functions.calc_rotational_force(mass_ave, omega_ave, radius_ave)
rot_force_uncert = functions.calc_rotational_force_uncertainty(mass_ave, omega_ave, radius_ave, mass_d, omega_d, radius_d)

# Output values
print("Mass: " + str(mass_ave) + " +/- " + str(mass_d))
print("Omega: " + str(omega_ave) + " +/- " + str(omega_d))
print("Radius: " + str(radius_ave) + " +/- " + str(radius_d))
print("Rotational Force: " + str(rot_force) + " +/- " + str(rot_force_uncert))
