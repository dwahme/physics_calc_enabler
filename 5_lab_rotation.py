import functions as f

##################
# BEGIN DATA INPUT
##################

# Add data here
mass_M = 0
mass_m = 0
radius_R = 0
radius_r = 0

mass_M_uncert = 0
mass_m_uncert = 0
radius_R_uncert = 0
radius_r_uncert = 0

fall_h = 0
fall_uncert = 0

################
# END DATA INPUT
################


# Run calculations

# Calculate basic theoretical values
disk_moment = f.calc_moment_inertia_disk(mass_M, radius_R)
tension_modifier = mass_m * radius_r * radius_r / disk_moment
tension_approx = f.calc_weight(mass_m)
tension_offset = 1 / (1 + tension_modifier)
tension = tension_approx * tension_offset

torque = tension * radius_r
# mom_inertia = disk_moment

alpha_0 = torque / disk_moment