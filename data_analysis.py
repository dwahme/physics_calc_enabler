import functions

#put ur number here ;)
vals = [1, 2, 3, 4]
mass = 1
omega = 1
radius = 1
d_mass = 1
d_omega = 1
d_radius = 1

avg = functions.get_average(vals)
uncert = functions.calc_uncertainty(vals)
rot_force = functions.calc_rotational_force(mass, omega, radius)
rot_force_uncert = functions.calc_rotational_force_uncertainty(mass, omega, radius, d_mass, d_omega, d_radius)

print("Average: " + str(avg))
print("Uncertainty: " + str(uncert))
print("Rotational Force:" + str(rot_force))
print("Rotational Force Uncertainty: " + str(rot_force_uncert))
