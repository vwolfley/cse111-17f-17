####################
# Date: 2022-11-05
# File: chemistry.py
# Author: Vern Wolfley
# Class: CSE 111
# Purpose: 07 Prove Milestone: Lists
# Write a program that uses lists and a dictionary to compute
# the molar mass of a chemical substance and the number of moles
# in a sample of that substance.
#####################

"""
Wite the main function that takes no parameters and returns nothing.
The main function should do the following:
    1. Call the make_periodic_table function and store the returned list in a variable.
    2. Print the name and atomic mass for each chemical element on a separate line. Do not print the chemical element symbols.
"""


def main():

    # Get a chemical formula for a molecule from the user.
    # formula = input("Please enter your chemical formula: ")

    # Get the mass of a chemical sample in grams from the user.
    # mass = float(input("Please enter the mass of the chemical sample in grams: "))

    #############################
    # TESTING ONLY
    # formula = "C6H12O6"
    # mass = 12.37
    formula = "C13H18O2"
    mass = 5.04
    # formula = "C6O2"
    # mass = 12.37
    ##################################

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table_dict = make_periodic_table()
    # print(periodic_table_dict)

    # Call the make_known_molecules_dict function and
    # store the molecules table in a variable.
    known_molecules_dict = make_known_molecules_dict()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(formula, periodic_table_dict)
    # print(symbol_quantity_list)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    total_molar_mass = compute_molar_mass(
        symbol_quantity_list, periodic_table_dict)

    # Call the get_formula_name function to find the formulas common name
    compound_name = get_formula_name(formula, known_molecules_dict)

    # Compute the number of moles in the sample.
    moles_in_sample = mass/total_molar_mass

    # Call the sum_protons function
    number_protons = sum_protons(symbol_quantity_list, periodic_table_dict)

    # Print the molar mass.
    print(f"Molar mass of {formula}: {total_molar_mass:,.5f} grams/mole")

    # Print the number of moles.
    print(f"Number of moles in the sample: {moles_in_sample:,.5f} moles")

    # Print the formulas compound name
    print(f"Compounds name is: {compound_name}")

    # Print the number of protons in the compound
    print(f"Number of protons in the compound: {number_protons}")


def make_known_molecules_dict():
    '''Creates and returns a dictionary that 
    contains known chemical formulas and their names
    Parameter:
        none
    Return: known_molecules_dict
    '''
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water",
        "C6H12O6": "glucose"
    }

    return known_molecules_dict


def make_periodic_table():
    '''Creates and returns a compound list
    Parameter:
        none
    Return: periodic_table_list
    '''
    periodic_table_dict = {
        # [symbol, name, atomic_mass, atomic_number]
        'Ac': ['Actinium', 227, 89],
        'Ag': ['Silver', 107.8682, 47],
        'Al': ['Aluminum', 26.9815386, 13],
        'Ar': ['Argon', 39.948, 18],
        'As': ['Arsenic', 74.9216, 33],
        'At': ['Astatine', 210, 85],
        'Au': ['Gold', 196.966569, 79],
        'B': ['Boron', 10.811, 5],
        'Ba': ['Barium', 137.327, 56],
        'Be': ['Beryllium', 9.012182, 4],
        'Bi': ['Bismuth', 208.9804, 83],
        'Br': ['Bromine', 79.904, 35],
        'C': ['Carbon', 12.0107, 6],
        'Ca': ['Calcium', 40.078, 20],
        'Cd': ['Cadmium', 112.411, 48],
        'Ce': ['Cerium', 140.116, 58],
        'Cl': ['Chlorine', 35.453, 17],
        'Co': ['Cobalt', 58.933195, 27],
        'Cr': ['Chromium', 51.9961, 24],
        'Cs': ['Cesium', 132.9054519, 55],
        'Cu': ['Copper', 63.546, 29],
        'Dy': ['Dysprosium', 162.5, 66],
        'Er': ['Erbium', 167.259, 68],
        'Eu': ['Europium', 151.964, 63],
        'F': ['Fluorine', 18.9984032, 9],
        'Fe': ['Iron', 55.845, 26],
        'Fr': ['Francium', 223, 87],
        'Ga': ['Gallium', 69.723, 31],
        'Gd': ['Gadolinium', 157.25, 64],
        'Ge': ['Germanium', 72.64, 32],
        'H': ['Hydrogen', 1.00794, 1],
        'He': ['Helium', 4.002602, 2],
        'Hf': ['Hafnium', 178.49, 72],
        'Hg': ['Mercury', 200.59, 80],
        'Ho': ['Holmium', 164.93032, 67],
        'I': ['Iodine', 126.90447, 53],
        'In': ['Indium', 114.818, 49],
        'Ir': ['Iridium', 192.217, 77],
        'K': ['Potassium', 39.0983, 19],
        'Kr': ['Krypton', 83.798, 36],
        'La': ['Lanthanum', 138.90547, 57],
        'Li': ['Lithium', 6.941, 3],
        'Lu': ['Lutetium', 174.9668, 71],
        'Mg': ['Magnesium', 24.305, 12],
        'Mn': ['Manganese', 54.938045, 25],
        'Mo': ['Molybdenum', 95.96, 42],
        'N': ['Nitrogen', 14.0067, 7],
        'Na': ['Sodium', 22.98976928, 11],
        'Nb': ['Niobium', 92.90638, 41],
        'Nd': ['Neodymium', 144.242, 60],
        'Ne': ['Neon', 20.1797, 10],
        'Ni': ['Nickel', 58.6934, 28],
        'Np': ['Neptunium', 237, 93],
        'O': ['Oxygen', 15.9994, 8],
        'Os': ['Osmium', 190.23, 76],
        'P': ['Phosphorus', 30.973762, 15],
        'Pa': ['Protactinium', 231.03588, 91],
        'Pb': ['Lead', 207.2, 82],
        'Pd': ['Palladium', 106.42, 46],
        'Pm': ['Promethium', 145, 61],
        'Po': ['Polonium', 209, 84],
        'Pr': ['Praseodymium', 140.90765, 59],
        'Pt': ['Platinum', 195.084, 78],
        'Pu': ['Plutonium', 244, 94],
        'Ra': ['Radium', 226, 88],
        'Rb': ['Rubidium', 85.4678, 37],
        'Re': ['Rhenium', 186.207, 75],
        'Rh': ['Rhodium', 102.9055, 45],
        'Rn': ['Radon', 222, 86],
        'Ru': ['Ruthenium', 101.07, 44],
        'S': ['Sulfur', 32.065, 16],
        'Sb': ['Antimony', 121.76, 51],
        'Sc': ['Scandium', 44.955912, 21],
        'Se': ['Selenium', 78.96, 34],
        'Si': ['Silicon', 28.0855, 14],
        'Sm': ['Samarium', 150.36, 62],
        'Sn': ['Tin', 118.71, 50],
        'Sr': ['Strontium', 87.62, 38],
        'Ta': ['Tantalum', 180.94788, 73],
        'Tb': ['Terbium', 158.92535, 65],
        'Tc': ['Technetium', 98, 43],
        'Te': ['Tellurium', 127.6, 52],
        'Th': ['Thorium', 232.03806, 90],
        'Ti': ['Titanium', 47.867, 22],
        'Tl': ['Thallium', 204.3833, 81],
        'Tm': ['Thulium', 168.93421, 69],
        'U': ['Uranium', 238.02891, 92],
        'V': ['Vanadium', 50.9415, 23],
        'W': ['Tungsten', 183.84, 74],
        'Xe': ['Xenon', 131.293, 54],
        'Y': ['Yttrium', 88.90585, 39],
        'Yb': ['Ytterbium', 173.054, 70],
        'Zn': ['Zinc', 65.38, 30],
        'Zr': ['Zirconium', 91.224, 40],
    }

    return periodic_table_dict


class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound
    list that stores the quantity of atoms of each element
    in the molecule. For example, this function will convert
    "H2O" to [["H", 2], ["O", 1]] and
    "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]

    Parameters
        formula: a string that contains a chemical formula
        periodic_table_dict: the compound dictionary returned
            from make_periodic_table
    Return: a compound list that contains chemical symbols and
        quantities like this [["Fe", 2], ["O", 3]]
    """
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elem_dict, symbol):
        return 0 if symbol not in elem_dict else elem_dict[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula, index+1, level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    curr = prev + group_dict[symbol] * quant
                    elem_dict[symbol] = curr
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError("invalid formula, "
                                           f"unknown element symbol: {symbol}",
                                           formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError("invalid formula, "
                                       "unmatched close parenthesis",
                                       formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError("invalid formula, "
                               "unmatched open parenthesis",
                               formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each each inner list in the
    # compound symbol_quantity_list:

    # 1. Separate the inner list into symbol and quantity.
    # print(symbol_quantity_list)
    symbol_list = [i[0] for i in symbol_quantity_list]
    quantity_list = [i[1] for i in symbol_quantity_list]
    # print(symbol_list, quantity_list)

    # 2. Get the atomic mass for the symbol from the dictionary.
    atomic_mass = []
    for i in symbol_list:
        values = periodic_table_dict[i]
        atomic_mass.append(values[1])
    # print(atomic_mass)

    # 3. Multiply the atomic mass by the quantity.
    molar_mass = []
    for (x, y) in zip(atomic_mass, quantity_list):
        molar_mass.append(x*y)
    # print(sum(molar_mass))

    # 4.  Add the product into the total molar mass.
    total_molar_mass = sum(molar_mass)

    # Return the total molar mass.
    return total_molar_mass


def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".

    Parameters
        formula: a string that contains a chemical formula
        known_molecules_dict: a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    # Check if the formula is a key that is in the known_molecules_dict.
    if formula in known_molecules_dict:

        # Find the name for the formula that the user wants.
        compound_name = known_molecules_dict[formula]

    else:
        # Print a message stating that the formula entered
        # by the user is not in the dictionary.
        compound_name = "Not Found in Dictionary!"

    return compound_name


def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict: the compound dictionary
            returned from make_periodic_table.
    Return: the total number of protons of all
        the elements in symbol_quantity_list.
    """
    # 1. Separate the inner list into symbol and quantity.
    # print(symbol_quantity_list)
    symbol_list = [i[0] for i in symbol_quantity_list]
    quantity_list = [i[1] for i in symbol_quantity_list]
    # atomic_number_list = [i[2] for i in symbol_quantity_list]
    # print(symbol_list, quantity_list)

    # 2. Get the atomic_number for the symbol from the dictionary.
    atomic_number = []
    for i in symbol_list:
        values = periodic_table_dict[i]
        atomic_number.append(values[2])
    # print(atomic_number)

    # 3. Multiply the atomic number by the quantity.
    num_protons = []
    for (x, y) in zip(atomic_number, quantity_list):
        num_protons.append(x*y)
    # print(sum(num_protons))

    # 4.  Add the product into the total num_protons.
    total_num_protons = sum(num_protons)

    # Return the total molar mass.
    return total_num_protons


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
