def compute_discount(quantity, price, discount_rate):
  discount_amount = quantity * price * discount_rate
  discounted_price = quantity * price - discount_amount
  return discount_amount, discounted_price

# Get input from the user
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))
discount_rate = float(input("Enter discount rate (as a decimal): "))

# Call the function to compute discount amount and discounted price
discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)

# Display the results
print("This is your quantity ", quantity)
print("Your price per item is ", price)
print("This is your discounted amount $ ", discount_amount)
print("This is your discounted price $ ", discounted_price)
