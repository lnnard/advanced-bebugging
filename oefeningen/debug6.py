def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
        
    return total / count

def main():
    numbers = [10, 20, 30, 40, 50]
    try:
        average = calculate_average(numbers)
        print(f"The average is: {average}")
    except ZeroDivisionError:
        print("Cannot calculate the average of an empty list.")

if __name__ == "__main__":
    main()
