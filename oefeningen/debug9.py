def calculate_total(prices):
    """
    Calculate the total price of items in the shopping cart.
    
    Args:
        prices (list): A list of item prices.
    """
    total = sum(prices)
    print(total)

def checkout(prices):
    """
    Simulate the checkout process and provide the total.
    
    Args:
        prices (list): A list of item prices.
    """
    total_price = calculate_total(prices)
    print(f"The total price is: {total_price}") 

# Example usage
items = [9.99, 19.99, 4.99, 3.50]
checkout(items)
