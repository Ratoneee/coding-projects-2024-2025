# Open and read the CSV file
with open('lifeexpectancy', 'r') as file:
    data = file.readlines()

# Initialize variables to track the min and max life expectancy values
min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')

# Process each line in the dataset
for line in data[1:]:  # Skip the header row
    parts = line.strip().split(',')
    
    # Assuming columns are [country, year, life_expectancy], adjust as needed
    country = parts[0]
    year = int(parts[1])
    life_expectancy = float(parts[2])
    
    # Check if this life expectancy is a new min or max
    if life_expectancy < min_life_expectancy:
        min_life_expectancy = life_expectancy
    if life_expectancy > max_life_expectancy:
        max_life_expectancy = life_expectancy

# Output the results
print(f"Min Life Expectancy: {min_life_expectancy}")
print(f"Max Life Expectancy: {max_life_expectancy}")
