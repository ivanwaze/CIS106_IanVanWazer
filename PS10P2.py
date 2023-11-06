#Definition  phase
def compute_square_footage(length, width, height):
  floor_ceiling_area = 2 * length * width
  wall1_area = 2 * length * height
  wall2_area = 2 * width * height

  total_area = floor_ceiling_area + wall1_area + wall2_area
  return total_area

def calculate_paint_gallons(square_footage):
  gallons_needed = square_footage / 50
  return gallons_needed

def main():
  while True:
      response = input("Do you want to run the program? (Yes or No): ").lower()
      if response != "yes":
          break

      length = float(input("Enter the length of the room (in feet): "))
      width = float(input("Enter the width of the room (in feet): "))
      height = float(input("Enter the height of the room (in feet): "))

      square_footage = compute_square_footage(length, width, height)
      gallons_needed = calculate_paint_gallons(square_footage)

      print(f"Square Footage of the room: {square_footage:.2f} sq. ft.")
      print(f"Gallons of paint needed: {gallons_needed:.2f}")

if __name__ == "__main__":
  main()
