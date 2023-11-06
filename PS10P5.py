def compute_assessed_value(county, market_value):
  assessed_value_percent = {
      'Cook': 0.90,
      'DuPage': 0.80,
      'McHenry': 0.75,
      'Kane': 0.60,
      'All others': 0.70
  }

  assessed_percent = assessed_value_percent.get(county, 0.70)
  assessed_value = market_value * assessed_percent
  return assessed_value

def main():
  total_market_values = 0
  total_assessed_values = 0

  while True:
      response = input("Do you want to run the program? (Yes or No): ").lower()
      if response != "yes":
          break

      county = input("Enter the county: ")
      market_value = float(input("Enter the market value of the home: "))

      assessed_value = compute_assessed_value(county, market_value)
      print(f"Assessed value: ${assessed_value:.2f}")

      total_market_values += market_value
      total_assessed_values += assessed_value

  print(f"\nTotal market value of all homes: ${total_market_values:.2f}")
  print(f"Total assessed value of all homes: ${total_assessed_values:.2f}")

if __name__ == "__main__":
  main()
