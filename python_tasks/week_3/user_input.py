def calculate_discount():
    user_input_price = int(input("Please enter the original price: "))
    user_input_discount = float(input("Please enter the discount percentage:"))
    discounted_price = ((100 - user_input_discount) / 100) * user_input_price
    print(f"The discounted price is: {discounted_price}")