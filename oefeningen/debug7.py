def calculate_ratio(numerator, denominator):
    """
    Calculate the ratio of two numbers.

    Args:
        numerator (float): The numerator of the ratio.
        denominator (float): The denominator of the ratio.

    Returns:
        float: The calculated ratio.
    """
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    
    return numerator / denominator

def main():
    
    numerator = 10
    denominator = 1
            
    result = calculate_ratio(numerator, denominator)
    print(f"The ratio is: {result}")
    
if __name__ == "__main__":
    main()
