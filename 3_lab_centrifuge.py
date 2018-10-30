import functions

# Add data here
time_1 = 1
mass_h = 0
mass_w = 0
radius_min = 0
radius_max = 0
mass_d = 0
time_d = 0
radius_d = 0

#note, these are 1 to avoid div by 0
times = [
    time_1, 1, 1, 1
]
weight_masses = [
    mass_w, 0, 0, 0
]

# best fit data
# input after creating the graph
x1 = 1 # to avoid div by 0
y1 = 0
x2 = 0
y2 = 0

# Calculate values
radius_values = [radius_min, radius_max]
omega_ave = functions.calc_omega(time_1)
radius_ave = functions.get_average(radius_values)
weight = functions.calc_weight(mass_w)
slope = functions.calc_slope(x1, y1, x2, y2)

# Calculate uncertainties
omega_d = functions.calc_omega_uncertainty(time_1, time_d)

# Run full rotational calculations
rot_force = functions.calc_rotational_force(mass_h, omega_ave, radius_ave)
rot_force_uncert = functions.calc_rotational_force_uncertainty(mass_h, omega_ave, radius_ave, mass_d, omega_d, radius_d)

# Output values
print("Mass: " + str(mass_h) + " +/- " + str(mass_d))
print("Omega: " + str(omega_ave) + " +/- " + str(omega_d))
print("Radius: " + str(radius_ave) + " +/- " + str(radius_d))
print("Rotational Force: " + str(rot_force) + " +/- " + str(rot_force_uncert))

# Generate graph table
for idx in range(0, 4):
    omega = functions.calc_omega(times[idx])
    omega_squared = omega * omega
    f_tension = 9.8 * weight_masses[idx]
    f_centripetal = functions.calc_rotational_force(weight_masses[idx], omega, radius_ave)

    print("Trial {}, Time: {}, Mass_w: {}, Omega: {}, Omega^2: {}, Force of tension: {}, Delta Omega: {}, Centripetal Force: {}".format(
        idx, times[idx], weight_masses[idx], omega, omega_squared, f_tension, omega_d, f_centripetal
    ))