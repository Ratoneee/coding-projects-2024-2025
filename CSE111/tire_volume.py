#added so after saving the date, time, and volume to 'volumes.txt', it auto-opens the file on windows and or mac os.
import math
from datetime import datetime
import os

#gets input from user
tire_width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio_tire = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_wheel = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#calc using the formula
calc = (math.pi * tire_width**2 * ratio_tire * (tire_width * ratio_tire + 2540 * diameter_wheel)) / 10_000_000_000
calc = round(calc, 2)  # Round to two decimal places

#displays current calc
print(f"The approximate volume is {calc:.2f} liters")

#gets current date
current_date = datetime.now().strftime("%Y-%m-%d")

#data to volumes.txt
file_name = "volumes.txt"
with open(file_name, "at") as file:
    file.write(f"{current_date}, {tire_width}, {ratio_tire}, {diameter_wheel}, {calc}\n")

print("Data has been saved to volumes.txt")

#open volumes.txt automatically after running code
if os.name == "nt":  #for windows os
    os.system(f"notepad {file_name}")
elif os.name == "posix":  #mac os
    os.system(f"open {file_name}")