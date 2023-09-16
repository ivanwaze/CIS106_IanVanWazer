#input phase
meal = float(input("What is the price of your meal?"))
#process phase
tipval1 = meal * 0.15
tipval2 = meal * 0.18
tipval3 = meal * 0.20
totval1 = meal + tipval1
totval2 = meal + tipval2
totval3 = meal + tipval3
#output phase
print("Your meal cost $", meal)
print("The tip for a 15% tip is", tipval1)
print("The tip for a 18% tip is", tipval2)
print("The tip for a 20% tip is", tipval3)
print("The total price for a 15% tip is", totval1)
print("The total price for a 18% tip is", totval2)
print("The total price for a 20% tip is", totval3)