import numpy as np

def generate_sequence(current, previous, terms_left):
    """
    Recursively generates a sequence of numbers where each number is 
    the sum of the previous two numbers.
    
    Args:
        current (int): The current number in the sequence.
        previous (int): The previous number in the sequence.
        terms_left (int): The number of terms left to generate.

    Returns:
        list: The sequence of numbers.
    """
    # Base case: Stop recursion when no terms are left
    if terms_left == 0:
        return []
    
    # Generate the next number and continue recursion
    next_number = current + previous
    return [current] + generate_sequence(next_number, current, terms_left - 1)

def main():
    start_value = 1  # The initial value
    terms = 100  # The number of terms to generate
    
    # Generate the sequence starting with the given value
    sequence = generate_sequence(start_value, 0, terms)
    print(f"Generated sequence: {sequence}")

if __name__ == "__main__":
    main()
