def compute_forecast(month, sales):
  forecast_percent = {
      'Jan': 0.10, 'Feb': 0.10, 'Mar': 0.10,
      'Apr': 0.15, 'May': 0.15, 'Jun': 0.15,
      'Jul': 0.20, 'Aug': 0.20, 'Sep': 0.20,
      'Oct': 0.25, 'Nov': 0.25, 'Dec': 0.25
  }

  forecast = sales * (1 + forecast_percent[month])
  return forecast

def main():
  while True:
      response = input("Do you want to run the program? (Yes or No): ").lower()
      if response != "yes":
          break

      last_name = input("Enter last name: ")
      month = input("Enter the month (Abbreviation, e.g., Jan, Feb, etc.): ")
      sales = float(input("Enter sales amount: "))

      next_month_sales = compute_forecast(month, sales)
      print(f"Next month's sales forecast: {next_month_sales:.2f}")

if __name__ == "__main__":
  main()
