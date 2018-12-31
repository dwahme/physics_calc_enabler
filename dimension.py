from physics.units import UNITS, Dimensional

vel_unit = UNITS.m / UNITS.s / UNITS.s

vel_0 = Dimensional(6, vel_unit)
vel_1 = Dimensional(4, vel_unit)

super_vel = vel_0 + vel_1

print("{} + {} = {}".format(vel_0, vel_1, super_vel))