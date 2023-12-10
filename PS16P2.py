class Car:
  def __init__(self, make, model, sticker_price):
      self.make = make
      self.model = model
      self.sticker_price = sticker_price

  def discount_price(self):
      return self.sticker_price * 0.9  # 90% of the sticker price


class Sport(Car):
  def __init__(self, make, model, sticker_price):
      super().__init__(make, model, sticker_price)
      self.option_prices = {
          'SportWheels': 1000.00,
          'SportEngine': 3000.00,
          'SportInterior': 2000.00
      }
      self.selected_options = {
          'SportWheels': False,
          'SportEngine': False,
          'SportInterior': False
      }

  def include_option(self, option):
      if option in self.option_prices:
          self.selected_options[option] = True
      else:
          print(f"{option} is not a valid option.")

  def pricewithoptions(self):
      total_price = self.discount_price()
      for option, selected in self.selected_options.items():
          if selected:
              total_price += self.option_prices[option]
      return total_price


# Test the classes
car = Car('Toyota', 'Camry', 30000)
print(f"Discounted Price for {car.make} {car.model}: ${car.discount_price()}")

sport_car = Sport('BMW', 'M3', 80000)
sport_car.include_option('SportWheels')
sport_car.include_option('SportEngine')
sport_car.include_option('SportInterior')
print(f"Price for {sport_car.make} {sport_car.model} with options: ${sport_car.pricewithoptions()}")
