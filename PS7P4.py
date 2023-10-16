f = open("P4d.txt", "r")

#initialize counters and sums to 0
count = 0.0
totextprice = 0.0

#get first data line
item =  (f.readline().rstrip('\n'))

while item != "":
  qty = float(f.readline())
  price = float(f.readline())

  extprice = qty * price
  # sum and count in the loop
  totextprice = totextprice + extprice
  count = count + 1

  # display a line of data
  print("Item is: ", item)
  print("Quantity is: ", qty)
  print("Price is: ", price)
  print("Extended price is: " , extprice)

  #get next price
  item = str(f.readline().rstrip('\n'))

# after the loop
# final calculations
# display them and sums and counts
print("Total extended prices:     ",totextprice)
print("Number of Orders:      ", count)
avg = totextprice / count
print(" Average Order is:    ", avg)
