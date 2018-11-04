import functions as f

##################
# BEGIN DATA INPUT
##################

mass_g1 = 0
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
g2_inelastic_times_0 = [
    0, 0
]
g1_inelastic_times_1 = [
    0, 0
]
g2_inelastic_times_1 = [
    0, 0
]
g1_inelastic_vels_0 = [
    0, 0
]
g2_inelastic_vels_0 = [
    0, 0
]
g1_inelastic_vels_1 = [
    0, 0
]
g2_inelastic_vels_1 = [
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


# Elastic collision calclations
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

# calculate predicted velocity after the collision
#todo: dawson pls ^
# compare prediction with measured

# Inelastic collision calculations
# for each inelastic collision, calc KE for g1 before collis
inelastic_KE_g1_0 = []
for col_vel in inelastic_velocities_g1:
    inelastic_KE_g1_0.append(f.calc_ke(mass_g1, col_vel))
# for each inelastic collision, calc KE for g1 after collis
inelastic_KE_g1_1 = []
for col_vel in inelastic_velocities_g1_g2:
    inelastic_KE_g1_1.append(f.calc_ke(mass_g1, col_vel))
# for each inelastic collision, calc KE for g2 before collis
inelastic_KE_g2_0 = [0 for _ in inelastic_velocities_g1]
# for each inelastic collision, calc KE for g2 after collis
inelastic_KE_g2_1 = []
for col_vel in inelastic_velocities_g1_g2:
    inelastic_KE_g2_1.append(f.calc_ke(mass_g2, col_vel))

print(inelastic_KE_g1_0)
print(inelastic_KE_g1_1)
print(inelastic_KE_g2_0)
print(inelastic_KE_g2_1)
# calc mean of KE's
# calc spread of KE's
