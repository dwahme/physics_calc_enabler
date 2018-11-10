import functions as f

##################
# BEGIN DATA INPUT
##################

# Add data here
mass_M = 0
mass_m = 0
radius_R = 0
radius_r = 0

################
# END DATA INPUT
################


# Run calculations
disk_moment = f.calc_moment_inertia_disk(mass_M, radius_R)
tension_modifier = mass_m * radius_r * radius_r / disk_moment
tension_approx = f.calc_weight(mass_m)
tension_offset = 1 / (1 + tension_approx)
