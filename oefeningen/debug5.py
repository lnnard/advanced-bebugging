def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)  

def main():
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {number} is: {factorial(number)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
