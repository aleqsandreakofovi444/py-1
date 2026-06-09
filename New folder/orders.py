def process_orders(orders, inventory):
    """
    ამუშავებს ორდერებს და აკლებს პროდუქტის ოდენობას საწყობიდან.
    
    Args:
        orders: ორდერების სია (დიქტები {"product": "...", "quantity": ...})
        inventory: საწყობის დიქტი {"product": stock}
    
    Returns:
        successful_orders: წარმატებულად დამუშავებული ორდერების სია
    
    Raises:
        ValueError: თუ პროდუქტი არ არის საწყობში ან საკმარისი ოდენობა არ არის
    """
    successful_orders = []

    for order in orders:
        product = order["product"]
        quantity = order["quantity"]

        if product not in inventory:
            raise ValueError(f"Product '{product}' not found in inventory")

        if quantity > inventory[product]:
            raise ValueError(f"Not enough stock for '{product}'")

        inventory[product] -= quantity
        successful_orders.append(order)

    return successful_orders
