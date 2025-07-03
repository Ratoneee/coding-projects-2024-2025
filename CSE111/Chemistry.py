from formula import parse_formula

NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Li": ["Lithium", 6.941],
        "Be": ["Beryllium", 9.0122],
        "B": ["Boron", 10.81],
        "C": ["Carbon", 12.0107],
        "N": ["Nitrogen", 14.0067],
        "O": ["Oxygen", 15.9994],
        "F": ["Fluorine", 18.9984032],
        "Ne": ["Neon", 20.1797],
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_molar_mass = 0.0
    for symbol, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass

def get_formula_name(formula, known_molecules_dict):
    return known_molecules_dict.get(formula, "unknown compound")

def sum_protons(symbol_quantity_list, periodic_table_dict):
    total_protons = 0
    for symbol, quantity in symbol_quantity_list:
        atomic_number = periodic_table_dict[symbol][2]
        total_protons += atomic_number * quantity
    return total_protons

def main():
    known_molecules_dict = {
        "H2O": "Water",
        "CO2": "Carbon Dioxide",
        "C6H6": "Benzene",
        "CH4": "Methane",
    }

    formula = input("Enter the molecular formula of the sample: ")
    mass = float(input("Enter the mass in grams of the sample: "))

    symbol_quantity_list = parse_formula(formula)

    periodic_table_dict = make_periodic_table()
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)

    number_of_moles = mass / molar_mass

    compound_name = get_formula_name(formula, known_molecules_dict)

    print(f"Compound: {compound_name}")
    print(f"Molar Mass: {molar_mass:.5f} grams/mole")
    print(f"Number of Moles: {number_of_moles:.5f} moles")

    total_protons = sum_protons(symbol_quantity_list, periodic_table_dict)
    print(f"Total Protons: {total_protons}")

if __name__ == "__main__":
    main()
