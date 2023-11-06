def compute_out_the_door_price(make, model, ev_code, msrp):
  percent_off = {
      'Honda Accord': 0.10,
      'Toyota Rav4': 0.15,
      'All electric vehicles': 0.30,
      'All other vehicles': 0.05
  }

  discount_percent = percent_off.get(model, 0.05) if ev_code == 'N' else 0.30
  new_msrp = msrp * (1 - discount_percent)
  total_with_tax = new_msrp * 1.07
  return total_with_tax

def main():
  total_msrp = 0
  total_sales_price = 0

  while True:
      response = input("Do you want to run the program? (Yes or No): ").lower()
      if response != "yes":
          break

      make = input("Enter the make of the automobile: ")
      model = input("Enter the model of the automobile: ")
      ev_code = input("Is it an electric vehicle? (Y or N): ").upper()
      msrp = float(input("Enter the MSRP (sticker price) of the automobile: "))

      out_the_door_price = compute_out_the_door_price(make, model, ev_code, msrp)
      print(f"Out the door price: {out_the_door_price:.2f}")

      total_msrp += msrp
      total_sales_price += out_the_door_price

  print(f"\nTotal MSRP of all cars: {total_msrp:.2f}")
  print(f"Total sales price of all cars: {total_sales_price:.2f}")

if __name__ == "__main__":
  main()
