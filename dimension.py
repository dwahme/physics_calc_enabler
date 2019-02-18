from physics.units import UNITS, Dimensional
import functions

accel_unit = UNITS.m / UNITS.s / UNITS.s

accel_0 = Dimensional(6, accel_unit)
accel_1 = Dimensional(4, accel_unit)

accel_sum = accel_0 + accel_1

print("{} + {} = {}".format(accel_0, accel_1, accel_sum))

time = Dimensional(3, UNITS.s)
dist = Dimensional(9, UNITS.m)

vel = dist / time
print(vel)
