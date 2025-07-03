def main():
    # Get user inputs and convert to floats
    start_miles = float(input("Enter the first odometer reading (miles): "))
    end_miles = float(input("Enter the second odometer reading (miles): "))
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    # Calculate miles per gallon
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

    # Convert to liters per 100km
    lp100k = lp100k_from_mpg(mpg)

    # Display the results
    print(f"Fuel efficiency: {mpg:.2f} miles per gallon")
    print(f"Fuel efficiency: {lp100k:.2f} liters per 100 km")

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    """
    if amount_gallons <= 0:
        return 0  # Avoid division by zero
    return (end_miles - start_miles) / amount_gallons

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100 kilometers."""
    if mpg <= 0:
        return 0  # Avoid division by zero
    return 235.215 / mpg  # Conversion formula

# Run the program
main()
