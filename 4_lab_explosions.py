import functions as f

##################
# BEGIN DATA INPUT
##################

mass_g1 = .3132
mass_g1_uncertainty = .00005
mass_g2 = .2122
mass_g2_uncertainty = .00005

# explosion measurements
flag_length = .1
g1_explode_times = [
    .284, .314, .313, .287, .301
]
g2_explode_times = [
    .424, .433, .419, .404, .416
]
g1_explode_velocities = [
    1, 0
]
g2_explode_velocities = [
    1, 0
]

# elastic collision measurements
g1_elastic_times_0 = [
    .204, .185, .195, .171, .177
]
g1_elastic_times_1 = [
    1.190 - .175, 1.061 - .160, 1.131 - .168, .977 -.148, 1.022 - .154
]
g2_elastic_times_1 = [
    .175, .160, .168, .148, .154
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
    .228, .222, .254, .233, .224
]
tot_inelastic_times_1 = [
    .782 / 2, .759 / 2, .869 / 2, .799 / 2, .762 / 2
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
v_ratio = mass_g2 / mass_g1

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

ave_explode_vel_ratio = g1_explode_vel_ave / g2_explode_vel_ave

# calculate KE before and after explosion
explode_ke_0 = [f.calc_ke(mass_g1, vel) for vel in g1_explode_velocities]
explode_ke_1 = [f.calc_ke(mass_g2, vel) for vel in g2_explode_velocities]
explode_ke_tot = [sum(x) for x in zip(explode_ke_0, explode_ke_1)]

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
    for vel in g1_elastic_vels_0]
g2_momentums_0 = [0
    for _ in g1_elastic_vels_0]
g1_momentums_1 = [f.calc_momentum(mass_g1, vel) 
    for vel in g1_elastic_vels_1]
g2_momentums_1 = [f.calc_momentum(mass_g2, vel) 
    for vel in g2_elastic_vels_1]

# Calculate total momentums before and after collisions
elastic_momentum_tot_0 = [sum(x) for x in zip(g1_momentums_0, g2_momentums_0)]
elastic_momentum_tot_1 = [sum(x) for x in zip(g1_momentums_1, g2_momentums_1)]

# Calculate mean momentum and spread
elastic_momentum_ave_0 = f.get_average(elastic_momentum_tot_0)
elastic_momentum_ave_1 = f.get_average(elastic_momentum_tot_1)
elastic_momentum_spread_0 = f.calc_uncertainty(elastic_momentum_tot_0) * 2
elastic_momentum_spread_1 = f.calc_uncertainty(elastic_momentum_tot_1) * 2

# Elastic KE calculations
elastic_KE_g1_0 = [f.calc_ke(mass_g1, col_vel) 
    for col_vel in g1_elastic_vels_0]
elastic_KE_g1_1 = [f.calc_ke(mass_g1, col_vel)
    for col_vel in g1_elastic_vels_1]
elastic_KE_g2_0 = [0 for _ in g1_elastic_vels_1]
elastic_KE_g2_1 = [f.calc_ke(mass_g2, col_vel)
    for col_vel in g2_elastic_vels_1]

elastic_KE_tot_0 = [sum(x) for x in zip(elastic_KE_g1_0, elastic_KE_g2_0)]
elastic_KE_tot_1 = [sum(x) for x in zip(elastic_KE_g1_1, elastic_KE_g2_1)]

# Calculate mean energy and spread
elastic_KE_ave_0 = f.get_average(elastic_KE_tot_0)
elastic_KE_ave_1 = f.get_average(elastic_KE_tot_1)
elastic_KE_spread_0 = f.calc_uncertainty(elastic_KE_tot_0) * 2
elastic_KE_spread_1 = f.calc_uncertainty(elastic_KE_tot_1) * 2


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
avg_inelastic_KE_g2_0 = f.get_average(inelastic_KE_g2_0)
avg_inelastic_KE_g1_1 = f.get_average(inelastic_KE_g1_1)
avg_inelastic_KE_g2_1 = f.get_average(inelastic_KE_g2_1)
# calc spread of KE's
spread_inelastic_KE_g1_0 = f.calc_uncertainty(inelastic_KE_g1_0) * 2
spread_inelastic_KE_g2_0 = f.calc_uncertainty(inelastic_KE_g2_0) * 2
spread_inelastic_KE_g1_1 = f.calc_uncertainty(inelastic_KE_g1_1) * 2
spread_inelastic_KE_g2_1 = f.calc_uncertainty(inelastic_KE_g2_1) * 2


# Report results

# Explosion results
print("***** Explosion results")
print("Expected explosion velocity ratio:", v_ratio)
if flag_length > 0:
    print("m1 explosion velocities", g1_explode_velocities)
    print("m2 explosion velocities", g2_explode_velocities)
print("Ave explosion velocity for m1:", g1_explode_vel_ave)
print("Ave explosion velocity for m2:", g2_explode_vel_ave)
print("Ave explosion velocity ratio:", ave_explode_vel_ratio)
print("Explosion velocity ratio uncertainty for m1:", g1_explode_vel_uncert)
print("Explosion velocity ratio uncertainty for m2:", g2_explode_vel_uncert)
print("KE of m1:", explode_ke_0)
print("KE of m2:", explode_ke_1)
print("Total KE for explosions:", explode_ke_tot)
print("")

# Elastic collision results
print("***** Elastic collision results")
print("times:", g1_elastic_times_1)
if flag_length > 0:
    print("m1 elastic velocities 0", g1_elastic_vels_0)
    print("m1 elastic velocities 1", g1_elastic_vels_1)
    print("m2 elastic velocities 1", g2_elastic_vels_1)
print("m1 momentums 0:", g1_momentums_0)
print("m2 momentums 0:", g2_momentums_0)
print("m1 momentums 1:", g1_momentums_1)
print("m2 momentums 1:", g2_momentums_1)
print("Initial total elastic momentum:", elastic_momentum_tot_0)
print("Final total elastic momentum:", elastic_momentum_tot_1)
print("Mean initial elastic momentum:", elastic_momentum_ave_0)
print("Mean final elastic momentum:", elastic_momentum_ave_1)
print("Mean initial elastic momentum spread:", elastic_momentum_spread_0)
print("Mean final elastic momentum spread:", elastic_momentum_spread_1)
print("KE 1 0:", elastic_KE_g1_0)
print("KE 2 0:", elastic_KE_g2_0)
print("KE 1 1:", elastic_KE_g1_1)
print("KE 2 1:", elastic_KE_g2_1)
print("KE tot 0", elastic_KE_tot_0)
print("KE tot 1", elastic_KE_tot_1)
print("Mean initial elastic KE:", elastic_KE_ave_0)
print("Mean final elastic KE:", elastic_KE_ave_1)
print("Mean initial elastic KE spread:", elastic_KE_spread_0)
print("Mean final elastic KE spread:", elastic_KE_spread_1)
print("")

# Inelastic collision results
print("***** Inelastic collision results")
print("actual tot times:", tot_inelastic_times_1)
if flag_length > 0:
    print("m1 initial velocities:", g1_inelastic_vels_0)
    print("Total final velocities:", tot_inelastic_vels_1)
print("Predicted velocities after collision:", inelastic_predicted_vels)
print("Prediction comparisons (percent diff):", inelastic_comparisons)
print("Explode velocity ratio:", ave_explode_vel_ratio)
print("Initial m1 KE:", inelastic_KE_g1_0)
print("Initial m2 KE:", inelastic_KE_g2_0)
print("Final m1 KE:", inelastic_KE_g1_1)
print("Final m2 KE:", inelastic_KE_g2_1)
print("Average initial KE:", avg_inelastic_KE_g1_0 + avg_inelastic_KE_g2_0)
print("Average final KE:", avg_inelastic_KE_g1_1 + avg_inelastic_KE_g2_1)
print("Average initial m1 KE spread:", spread_inelastic_KE_g1_0 + spread_inelastic_KE_g2_0)
print("Average final m1 KE spread:", spread_inelastic_KE_g1_1 + spread_inelastic_KE_g2_1)