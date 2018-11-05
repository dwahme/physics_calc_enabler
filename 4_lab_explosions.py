import functions as f

##################
# BEGIN DATA INPUT
##################

mass_g1 = 1
mass_g1_uncertainty = 0
mass_g2 = 1
mass_g2_uncertainty = 0

# explosion measurements
flag_length = 0
g1_explode_times = [
    0, 0
]
g2_explode_times = [
    0, 0
]
g1_explode_velocities = [
    0, 0
]
g2_explode_velocities = [
    0, 0
]

# elastic collision measurements
g1_elastic_times_0 = [
    0, 0
]
g1_elastic_times_1 = [
    0, 0
]
g2_elastic_times_1 = [
    0, 0
]
g1_elastic_vels_0 = [
    0, 0
]
g1_elastic_vels_1 = [
    0, 0
]
g2_elastic_vels_1 = [
    0, 0
]

# inelastic collision measurements
g1_inelastic_times_0 = [
    0, 0
]
tot_inelastic_times_1 = [
    0, 0
]
g1_inelastic_vels_0 = [
    1, 1
]
tot_inelastic_vels_1 = [
    0, 0
]

################
# END DATA INPUT
################


# CALCULATIONS

# Explosion calculations
# predict the ratio of the velocities of the gliders using masses
v_ratio = mass_g1 / mass_g2

# Calculate velocites if necessary
if flag_length > 0:
    g1_explode_velocities = [f.calc_velocity(flag_length, time)
        for time in g1_explode_times]
    g2_explode_velocities = [f.calc_velocity(flag_length, time)
        for time in g2_explode_times]

# Get explosion velocities and uncertainties
g1_explode_vel_ave = f.get_average(g1_explode_velocities)
g2_explode_vel_ave = f.get_average(g2_explode_velocities)
g1_explode_vel_uncert = f.calc_uncertainty(g1_explode_velocities)
g2_explode_vel_uncert = f.calc_uncertainty(g2_explode_velocities)

# calculate KE before and after explosion
explode_ke_0 = f.calc_ke(mass_g1, 0) + f.calc_ke(mass_g2, 0)
explode_ke_1 = f.calc_ke(mass_g1, g1_explode_vel_ave) + f.calc_ke(mass_g2, g2_explode_vel_ave)


# Elastic collision calculations
# Calculate velocites if necessary
if flag_length > 0:
    g1_elastic_vels_0 = [f.calc_velocity(flag_length, time)
        for time in g1_elastic_times_0]
    g1_elastic_vels_1 = [f.calc_velocity(flag_length, time)
        for time in g1_elastic_times_1]
    g2_elastic_vels_1 = [f.calc_velocity(flag_length, time)
        for time in g2_elastic_times_1]

# Calculate momentum of gliders before and after collisions
g1_momentums_0 = [f.calc_momentum(mass_g1, vel) 
    for vel in g1_elastic_times_0]
g2_momentums_0 = [0
    for _ in g1_elastic_times_0]
g1_momentums_1 = [f.calc_momentum(mass_g1, vel) 
    for vel in g1_elastic_times_1]
g2_momentums_1 = [f.calc_momentum(mass_g2, vel) 
    for vel in g2_elastic_times_1]

# Calculate total momentums before and after collisions
elastic_momentum_tot_0 = [sum(x) for x in zip(g1_momentums_0, g2_momentums_0)]
elastic_momentum_tot_1 = [sum(x) for x in zip(g1_momentums_1, g2_momentums_1)]

# Calculate mean momentum and spread
elastic_momentum_ave_0 = f.get_average(elastic_momentum_tot_0)
elastic_momentum_ave_1 = f.get_average(elastic_momentum_tot_1)
elastic_momentum_spread_0 = f.calc_uncertainty(elastic_momentum_tot_0) * 2
elastic_momentum_spread_1 = f.calc_uncertainty(elastic_momentum_tot_1) * 2


# Inelastic collision calculations
# Calculate velocites if necessary
if flag_length > 0:
    g1_inelastic_vels_0 = [f.calc_velocity(flag_length, time)
        for time in g1_inelastic_times_0]
    tot_inelastic_vels_1 = [f.calc_velocity(flag_length, time)
        for time in tot_inelastic_times_1]

# calculate predicted velocity after the collision
def predict_velocity(v0, m1, m2):
    return m1 * v0 / (m1 + m2)

inelastic_predicted_vels = [predict_velocity(vel, mass_g1, mass_g2)
    for vel in g1_inelastic_vels_0]

# compare prediction with measured
inelastic_comparisons = [f.percent_diff(x[0], x[1])
    for x in zip(inelastic_predicted_vels, tot_inelastic_vels_1)]

# Calculate KE for g1 and total before and after collision
inelastic_KE_g1_0 = [f.calc_ke(mass_g1, col_vel) 
    for col_vel in g1_inelastic_vels_0]
inelastic_KE_g1_1 = [f.calc_ke(mass_g1, col_vel)
    for col_vel in tot_inelastic_vels_1]
inelastic_KE_g2_0 = [0 for _ in g1_inelastic_vels_0]
inelastic_KE_g2_1 = [f.calc_ke(mass_g2, col_vel)
    for col_vel in tot_inelastic_vels_1]

# calc mean of KE's
avg_inelastic_KE_g1_0 = f.get_average(inelastic_KE_g1_0)
avg_inelastic_KE_g1_1 = f.get_average(inelastic_KE_g1_1)
avg_inelastic_KE_g2_0 = f.get_average(inelastic_KE_g2_0)
avg_inelastic_KE_g2_1 = f.get_average(inelastic_KE_g2_1)
# calc spread of KE's
spread_inelastic_KE_g1_0 = f.calc_uncertainty(inelastic_KE_g1_0) * 2
spread_inelastic_KE_g1_1 = f.calc_uncertainty(inelastic_KE_g1_1) * 2
spread_inelastic_KE_g2_0 = f.calc_uncertainty(inelastic_KE_g2_0) * 2
spread_inelastic_KE_g2_1 = f.calc_uncertainty(inelastic_KE_g2_1) * 2
