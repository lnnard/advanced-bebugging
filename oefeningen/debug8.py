def print_list_items(numbers):
    """
    Print each item in the list of numbers.
    
    Args:
        numbers (list): A list of numbers.
    """
    for i in range(len(numbers)):
        print(numbers[i])

def main():
    numbers = [10, 20, 30, 40, 50]  # A simple list of numbers
    try:
        print_list_items(numbers)
    except IndexError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
