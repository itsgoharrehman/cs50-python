# Einstein
import math

speed_of_light = 300000000
mass = int(input("Enter mass in kg: "))

energy = mass * math.pow(speed_of_light, 2)
print(f"Energy equivalent of {mass} kilograms is {energy: .0f} Joules")
