def add_to_cart(item_name=input("Enter item name (or 'done' to finish): "), price=float(input("Enter item price: ")), *args, **kwargs):
    cart = {}
    total_cost_of_items = 0
    
    if item_name in cart:
        print(f'{item_name} is a duplicate')
        return
    
    final_price = price
    for discount in args:
        print('discount')
        discount = int(input("Enter discounts (if any, separated by spaces): "))
        final_price -= price * (discount / 100)
    
    cart[item_name] = {
        'price': round(final_price, 2),
        'details': kwargs
    }
    return 'working'
    
add_to_cart()
    
    # print('\n--- Cart Summary ---')
    # for item, details in cart.items():
        
