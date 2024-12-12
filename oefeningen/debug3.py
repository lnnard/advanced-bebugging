def calculate_total(cart_items):
    """
    Calculate the total cost of items in a shopping cart.
    
    Args:
        cart_items (list): A list of tuples where each tuple contains the item name (str) and price (float or int).
    
    Returns:
        float: The total cost of the items.
    """
    total = 0
    for item, price in cart_items:
        print(f"Adding {item} with price {price} to total.")
        total += price
    return total

def main():
    
    shopping_cart = [
        ("Apples", 3.50),
        ("Bananas", 2.75),
        ("Cherries", 5.00)
    ]
    
    try:
        total = calculate_total(shopping_cart)
        print(f"The total cost is: ${total:.2f}")
    except TypeError as e:
        print("A TypeError occurred while calculating the total:")
        print(e)

if __name__ == "__main__":
    main()
