# George Klein
# CBIS 4210
# Assignment 1.1
# 9/1/2024


# Function to calculate monthly revenue
# Calculate total monthly revenue based on units sold and price per unit.
def calculate_monthly_revenue(units_sold, price_per_unit):
    return units_sold * price_per_unit

# Main function to run the program
def main():
    units_sold = 150  # Example: 150 units sold in a month
    price_per_unit = 50.0  # Example: Each unit is sold for $50
    monthly_revenue = calculate_monthly_revenue(units_sold, price_per_unit)
    print(f"Monthly Revenue: ${monthly_revenue:.2f}")

# Call the main function
if __name__ == "__main__":
    main()

