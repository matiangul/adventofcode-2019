import day_1


def test_small_mass_fuel_requirement():
    assert day_1.calculate_fuel_to_carry_mass(-10) == 0
    assert day_1.calculate_fuel_to_carry_mass(0) == 0
    assert day_1.calculate_fuel_to_carry_mass(5) == 0


def test_mass_fuel_requirement():
    assert day_1.calculate_fuel_to_carry_mass(12) == 2
    assert day_1.calculate_fuel_to_carry_mass(14) == 2
    assert day_1.calculate_fuel_to_carry_mass(1969) == 654
    assert day_1.calculate_fuel_to_carry_mass(100756) == 33583


def test_small_mass_overall_fuel_requirement():
    assert day_1.calculate_fuel_to_carry_mass_with_fuel(-10) == 0
    assert day_1.calculate_fuel_to_carry_mass_with_fuel(0) == 0
    assert day_1.calculate_fuel_to_carry_mass_with_fuel(5) == 0


def test_overall_fuel_requirement():
    assert day_1.calculate_fuel_to_carry_mass_with_fuel(14) == 2
    assert day_1.calculate_fuel_to_carry_mass_with_fuel(1969) == 966
    assert day_1.calculate_fuel_to_carry_mass_with_fuel(100756) == 50346
