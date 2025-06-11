# -*- coding: utf-8 -*-

class CompositeElement:
    def __init__(self, name):
        self.name = name
        self._composite = None
    
    def composite(self):
        return self._composite
    
    def set_composite(self, other):
        self._composite = other

class CompositeMapping:
    def __init__(self):
        self.elements = {}
    
    def add_pair(self, element1, element2):
        # Create CompositeElement instances if they don't exist
        if element1 not in self.elements:
            self.elements[element1] = CompositeElement(element1)
        if element2 not in self.elements:
            self.elements[element2] = CompositeElement(element2)
        
        # Set up the composite relationship
        self.elements[element1].set_composite(self.elements[element2])
        self.elements[element2].set_composite(self.elements[element1])
    
    def get_element(self, name):
        return self.elements.get(name)

def check_encoding():
    """Check if the file is properly encoded in UTF-8"""
    try:
        # Try to encode and decode a Greek character
        test_char = 'α'
        test_char.encode('utf-8').decode('utf-8')
        return True
    except UnicodeError:
        print("Warning: There might be encoding issues with Greek characters")
        return False

def safe_print(text):
    """Safely print text that might contain special characters"""
    try:
        print(text)
    except Exception as e:
        print(f"Error printing: {str(e)}")
        # Fallback to repr() for problematic characters
        print(repr(text))

def print_with_prime_coloring(text):
    """Print text with prime elements in blue color"""
    # ANSI color codes
    BLUE = '\033[94m'
    RESET = '\033[0m'
    
    # Split the text into parts and color the prime elements
    parts = text.split('_prime')
    if len(parts) > 1:
        # If there's a prime element, color it
        colored_text = parts[0] + BLUE + '_prime' + RESET + parts[1]
        safe_print(colored_text)
    else:
        safe_print(text)

def demonstrate_composite_mapping():
    # Check encoding first
    if not check_encoding():
        print("Please ensure this file is saved with UTF-8 encoding")
        return

    # Create a composite mapping
    mapping = CompositeMapping()
    
    # Define all the letter sets
    latin_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    latin_lower = 'abcdefghijklmnopqrstuvwxyz'
    greek_upper = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ'
    greek_lower = 'αβγδεζηθικλμνξοπρστυφχψω'
    
    # Define Latin names
    latin_names_upper = [
        'ALPHA', 'BETA', 'GAMMA', 'DELTA', 'EPSILON', 'ZETA', 'ETA', 'THETA',
        'IOTA', 'KAPPA', 'LAMBDA', 'MU', 'NU', 'XI', 'OMICRON', 'PI', 'RHO',
        'SIGMA', 'TAU', 'UPSILON', 'PHI', 'CHI', 'PSI', 'OMEGA'
    ]
    latin_names_lower = [name.lower() for name in latin_names_upper]
    
    # Add all pairs
    safe_print("Creating composite mappings...")
    
    try:
        # 1. Latin uppercase to uppercase prime
        for letter in latin_upper:
            mapping.add_pair(letter, f"{letter}_prime")
        
        # 2. Latin lowercase to lowercase prime
        for letter in latin_lower:
            mapping.add_pair(letter, f"{letter}_prime")
        
        # 3. Greek uppercase to uppercase prime
        for letter in greek_upper:
            mapping.add_pair(letter, f"{letter}_prime")
        
        # 4. Greek lowercase to lowercase prime
        for letter in greek_lower:
            mapping.add_pair(letter, f"{letter}_prime")
        
        # 5. Latin names uppercase to uppercase prime
        for name in latin_names_upper:
            mapping.add_pair(name, f"{name}_prime")
        
        # 6. Latin names lowercase to lowercase prime
        for name in latin_names_lower:
            mapping.add_pair(name, f"{name}_prime")
        
        # Demonstrate the mappings
        safe_print("\nDemonstrating composite relationships:")
        
        # Example for first letter (A/α/alpha)
        safe_print("\nExample for first letter (A/α/alpha):")
        print_with_prime_coloring(f"A.composite() = {mapping.get_element('A').composite().name}")
        print_with_prime_coloring(f"A_prime.composite() = {mapping.get_element('A_prime').composite().name}")
        print_with_prime_coloring(f"a.composite() = {mapping.get_element('a').composite().name}")
        print_with_prime_coloring(f"a_prime.composite() = {mapping.get_element('a_prime').composite().name}")
        print_with_prime_coloring(f"Α.composite() = {mapping.get_element('Α').composite().name}")
        print_with_prime_coloring(f"Α_prime.composite() = {mapping.get_element('Α_prime').composite().name}")
        print_with_prime_coloring(f"α.composite() = {mapping.get_element('α').composite().name}")
        print_with_prime_coloring(f"α_prime.composite() = {mapping.get_element('α_prime').composite().name}")
        print_with_prime_coloring(f"ALPHA.composite() = {mapping.get_element('ALPHA').composite().name}")
        print_with_prime_coloring(f"ALPHA_prime.composite() = {mapping.get_element('ALPHA_prime').composite().name}")
        print_with_prime_coloring(f"alpha.composite() = {mapping.get_element('alpha').composite().name}")
        print_with_prime_coloring(f"alpha_prime.composite() = {mapping.get_element('alpha_prime').composite().name}")
        
        # Example for second letter (B/β/beta)
        safe_print("\nExample for second letter (B/β/beta):")
        print_with_prime_coloring(f"B.composite() = {mapping.get_element('B').composite().name}")
        print_with_prime_coloring(f"B_prime.composite() = {mapping.get_element('B_prime').composite().name}")
        print_with_prime_coloring(f"b.composite() = {mapping.get_element('b').composite().name}")
        print_with_prime_coloring(f"b_prime.composite() = {mapping.get_element('b_prime').composite().name}")
        print_with_prime_coloring(f"Β.composite() = {mapping.get_element('Β').composite().name}")
        print_with_prime_coloring(f"Β_prime.composite() = {mapping.get_element('Β_prime').composite().name}")
        print_with_prime_coloring(f"β.composite() = {mapping.get_element('β').composite().name}")
        print_with_prime_coloring(f"β_prime.composite() = {mapping.get_element('β_prime').composite().name}")
        print_with_prime_coloring(f"BETA.composite() = {mapping.get_element('BETA').composite().name}")
        print_with_prime_coloring(f"BETA_prime.composite() = {mapping.get_element('BETA_prime').composite().name}")
        print_with_prime_coloring(f"beta.composite() = {mapping.get_element('beta').composite().name}")
        print_with_prime_coloring(f"beta_prime.composite() = {mapping.get_element('beta_prime').composite().name}")
        
    except Exception as e:
        safe_print(f"Error during mapping creation: {str(e)}")
        return

if __name__ == "__main__":
    demonstrate_composite_mapping() 