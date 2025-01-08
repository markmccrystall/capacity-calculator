import re

def parse_formula(formula):
    # Handle nested parentheses
    while True:
        # Find the innermost parentheses and expand them
        match = re.search(r'\(([^\(\)]+)\)(\d*)', formula)
        if not match:
            break
        inner_formula, multiplier = match.groups()
        multiplier = int(multiplier) if multiplier else 1
        expanded = inner_formula * multiplier
        formula = formula[:match.start()] + expanded + formula[match.end():]

    return formula

def calculate_molecular_weight(parsed_formula, weights, rounding_digits=4):
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', parsed_formula)
    total_weight = 0.0

    for element, count in elements:
        count = int(count) if count else 1
        weight = weights.get(element, 0.0) * count
        total_weight += round(weight, rounding_digits)

    return total_weight

def calculate_theoretical_capacity(parsed_formula, weights, capacities, rounding_digits=4):
    elements = re.findall(r'([A-Z][a-z]*)(\d*)', parsed_formula)
    total_weight = 0.0
    weighted_capacity = 0.0

    for element, count in elements:
        count = int(count) if count else 1
        element_weight = weights.get(element, 0.0) * count
        element_capacity = capacities.get(element, 0.0)
        total_weight += round(element_weight, rounding_digits)
        weighted_capacity += round(element_weight * element_capacity, rounding_digits)

    if total_weight == 0:
        return 0

    theoretical_capacity = int(round(weighted_capacity / total_weight, rounding_digits))
    return theoretical_capacity

weights = {
    'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81, 'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
    'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974, 'S': 32.06, 'Cl': 35.45, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
    'Sc': 44.956, 'Ti': 47.867, 'V': 50.942, 'Cr': 51.996, 'Mn': 54.938, 'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693, 'Cu': 63.546,
    'Zn': 65.38, 'Ga': 69.723, 'Ge': 72.630, 'As': 74.922, 'Se': 78.971, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.468, 'Sr': 87.62,
    'Y': 88.906, 'Zr': 91.224, 'Nb': 92.906, 'Mo': 95.95, 'Tc': 98, 'Ru': 101.07, 'Rh': 102.91, 'Pd': 106.42, 'Ag': 107.87,
    'Cd': 112.41, 'In': 114.82, 'Sn': 118.71, 'Sb': 121.76, 'Te': 127.60, 'I': 126.90, 'Xe': 131.29, 'Cs': 132.91, 'Ba': 137.33,
    'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24, 'Pm': 145, 'Sm': 150.36, 'Eu': 151.96, 'Gd': 157.25, 'Tb': 158.93,
    'Dy': 162.50, 'Ho': 164.93, 'Er': 167.26, 'Tm': 168.93, 'Yb': 173.05, 'Lu': 174.97, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84,
    'Re': 186.21, 'Os': 190.23, 'Ir': 192.22, 'Pt': 195.08, 'Au': 196.97, 'Hg': 200.59, 'Tl': 204.38, 'Pb': 207.2, 'Bi': 208.98,
    'Po': 209, 'At': 210, 'Rn': 222, 'Fr': 223, 'Ra': 226, 'Ac': 227, 'Th': 232
}

capacities = {
    'Li': 3861, 'C': 372, 'Mg': 195, 'Al': 993, 'Si': 3579, 'P': 2596, 'S': 1675, 'Zn': 410, 'Ga': 769, 'Ge': 1384,
    'As': 1073, 'Se': 678, 'Br': 335, 'Ag': 248, 'Cd': 238, 'In': 1012, 'Sn': 960, 'Sb': 660, 'Te': 420, 'I': 211,
    'Au': 510, 'Pb': 550, 'Bi': 385
}

while True:
    raw_input = input("Enter a formula: ")
    parsed_formula = parse_formula(raw_input)
    molecular_weight = calculate_molecular_weight(parsed_formula, weights)
    theoretical_capacity = calculate_theoretical_capacity(parsed_formula, weights, capacities)
    
    print(f"The theoretical Li-storing capacity of {raw_input} is {theoretical_capacity} mAh/g")
    print()
