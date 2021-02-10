import tinyik
import numpy as np

arm = tinyik.Actuator(['z', [0., 0., 231.5], 'y', [0., 0., 221.], 'y', [0., 0., 129.5], 'z', [0., 0., 98.]])

print("")
print("---  1. hareket")
arm.ee = [270., 0., 330.]
print(arm.angles)
print(np.degrees(arm.angles).round(1))
print("")
print("---  2. hareket")
arm.ee = [270., 0., 400.]
print(arm.angles)
print(np.degrees(arm.angles).round(1))

