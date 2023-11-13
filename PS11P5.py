total = 0.10
tax = 0.10
def comptotal(qty,price):
  global total
  total = qty * price
  global tax 
  tax = total * 0.07
  return 



qty = float(input("Enter quantity of item "))
price = float(input("Enter price per unit"))
comptotal(qty,price)
print("Your total is $  ", total)
print("Your tax is $  ", tax)
