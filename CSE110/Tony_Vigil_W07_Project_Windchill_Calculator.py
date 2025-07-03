#I added so if the temp is below a certain value then it will display how cold it is so if the temp is below a ceratin number then it will display a warning if it really cold for example.
def calculate_windchill(temp, wind_speed):
    return 35.74 + 0.6215 * temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp * (wind_speed ** 0.16)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Function that shows feedback dependent on how cold it is
def windchill_feedback(windchill):
    if windchill <= -40:
        return "Dangerously cold! Stay indoors if possible."
    elif -40 < windchill <= -20:
        return "Very cold! Risk of frostbite in minutes."
    elif -20 < windchill <= 0:
        return "Cold! Be cautious, frostbite can happen quickly."
    elif 0 < windchill <= 32:
        return "Chilly, but manageable with proper clothing."
    else:
        return "Mild wind chill, a good day to be outside."

#Main program
def main():
    temp = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

    if unit == 'C':
        temp = celsius_to_fahrenheit(temp)
    
    for wind_speed in range(5, 61, 5):
        windchill = calculate_windchill(temp, wind_speed)
        feedback = windchill_feedback(windchill)
        print(f"At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {windchill:.2f}F")
        print(f"tempture description: {feedback}\n")

#Run program on start
main()
