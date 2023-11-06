def compute_ticket_price(miles):
  if miles >= 30:
      return 12
  elif miles >= 20:
      return 10
  elif miles >= 10:
      return 8
  else:
      return 5

def main():
  total_ticket_price = 0

  while True:
      response = input("Do you want to run the program? (Yes or No): ").lower()
      if response != "yes":
          break

      last_name = input("Enter your last name: ")
      miles = int(input("Enter miles from downtown Chicago: "))

      ticket_price = compute_ticket_price(miles)
      print(f"Ticket price for {last_name}: ${ticket_price}")

      total_ticket_price += ticket_price

  print(f"\nTotal ticket price for all passengers: ${total_ticket_price}")

if __name__ == "__main__":
  main()
