import functions as f

##################
# BEGIN DATA INPUT
##################

mass_g1 = 0
mass_g1_uncertainty = 0
mass_g2 = 1
mass_g2_uncertainty = 0

# explosion measurements
explode_flag_length = 0
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
elastic_flag_length = 0
g1_initial_times = [
    0, 0
]
g2_initial_times = [
    0, 0
]
g1_final_times = [
    0, 0
]
g2_final_times = [
    0, 0
]
g1_initial_velocities = [
    0, 0
]
g2_initial_velocities = [
    0, 0
]
g1_final_velocities = [
    0, 0
]
g2_final_velocities = [
    0, 0
]

################
# END DATA INPUT
################


# CALCULATIONS

# predict the ratio of the velocities of the gliders using masses
v_ratio = mass_g1 / mass_g2

# Calculate velocites if necessary
if explode_flag_length > 0:
    g1_explode_velocities = [f.calc_velocity(explode_flag_length, time)
        for time in g1_explode_times]
    g2_explode_velocities = [f.calc_velocity(explode_flag_length, time)
        for time in g2_explode_times]

# Get explosion velocities and uncertainties
g1_explode_vel_ave = f.get_average(g1_explode_velocities)
g2_explode_vel_ave = f.get_average(g2_explode_velocities)
g1_explode_vel_uncert = f.calc_uncertainty(g1_explode_velocities)
g2_explode_vel_uncert = f.calc_uncertainty(g2_explode_velocities)

# calculate KE before and after explosion
explode_ke_0 = f.calc_ke(mass_g1, 0) + f.calc_ke(mass_g2, 0)
explode_ke_1 = f.calc_ke(mass_g1, g1_explode_vel_ave) + f.calc_ke(mass_g2, g2_explode_vel_ave)

# if flag_length != 0, then need to calc velocities from times
    # calculate g1 velocities after the elastic collision
    # calculate g2 velocities after the elastic collision

# calculate predicted velocity after the collision
inelastic_velocities_g1 = [
    0, 0
]
inelastic_velocities_g1_g2 = [
    0, 0
]
#todo: dawson pls ^
# compare prediction with measured

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
