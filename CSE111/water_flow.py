import math

WATER_DENSITY = 998.2
GRAVITY = 9.80665
WATER_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    return tower_height + (tank_height / 2)

def pressure_gain_from_water_height(height):
    return WATER_DENSITY * GRAVITY * height / 1000

def pressure_loss_from_pipe(length, diameter, velocity, friction_factor):
    return -(friction_factor * length * WATER_DENSITY * velocity**2) / (2000 * diameter)

def pressure_loss_from_fittings(velocity, quantity):
    k_factor = 0.04
    return -(k_factor * quantity * WATER_DENSITY * velocity**2) / 2000

def reynolds_number(diameter, velocity):
    return (WATER_DENSITY * diameter * velocity) / WATER_VISCOSITY

def pressure_loss_from_pipe_reduction(diameter1, velocity1, reynolds, diameter2):
    k = (1 - (diameter2 / diameter1)**4)**2
    return -(k * WATER_DENSITY * velocity1**2) / 2000

def kpa_to_psi(kpa):
    return kpa * 0.1450377377338

def main():
    tower_height = float(input("enter tower height: "))
    tank_height = float(input("enter tank height: "))
    pipe_length = float(input("enter pipe length: "))
    pipe_diameter = float(input("enter pipe diameter: "))
    water_velocity = float(input("enter water velocity: "))
    friction_factor = float(input("enter friction factor: "))
    fittings = int(input("enter number of fittings: "))
    diameter2 = float(input("enter second pipe diameter: "))

    height = water_column_height(tower_height, tank_height)
    pressure_height = pressure_gain_from_water_height(height)
    pressure_pipe = pressure_loss_from_pipe(pipe_length, pipe_diameter, water_velocity, friction_factor)
    pressure_fittings = pressure_loss_from_fittings(water_velocity, fittings)
    reynolds = reynolds_number(pipe_diameter, water_velocity)
    pressure_reduction = pressure_loss_from_pipe_reduction(pipe_diameter, water_velocity, reynolds, diameter2)
    final_pressure = pressure_height + pressure_pipe + pressure_fittings + pressure_reduction
    final_pressure_psi = kpa_to_psi(final_pressure)

    print(f"final pressure: {final_pressure:.2f} kpa")
    print(f"final pressure: {final_pressure_psi:.2f} psi")

if __name__ == "__main__":
    main()
