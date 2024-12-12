def calculate_ratio(numerator, denominator):
    """
    Calculate the ratio of two numbers.

    Args:
        numerator (float): The numerator of the ratio.
        denominator (float): The denominator of the ratio.

    Returns:
        float: The calculated ratio.
    """
    return numerator / denominator

def main():
    
    try:
        numerator = 10
        denominator = 0
        
        
        result = calculate_ratio(numerator, denominator)
        print(f"The ratio is: {result}")
    except Exception:
        print("error happened")

if __name__ == "__main__":
    main()
