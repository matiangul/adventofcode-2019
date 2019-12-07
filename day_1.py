from math import floor
from sys import stdin


def calculate_fuel_to_carry_mass(mass):
    return max(0, floor(mass / 3) - 2)


def calculate_fuel_to_carry_mass_with_fuel(mass):
    fuel = 0
    remaining_mass = mass
    while remaining_mass > 6:
        remaining_mass = calculate_fuel_to_carry_mass(remaining_mass)
        fuel += remaining_mass
    return fuel


if __name__ == "__main__":
    module_fuel = 0
    overall_fuel = 0
    for line in stdin:
        module_mass = int(line)
        module_fuel += calculate_fuel_to_carry_mass(module_mass)
        overall_fuel += calculate_fuel_to_carry_mass_with_fuel(module_mass)
    print("Part 1: ", module_fuel)
    print("Part 2: ", overall_fuel)
