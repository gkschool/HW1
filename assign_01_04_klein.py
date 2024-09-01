# George Klein
# CBIS 4210
# Assignment 1.1
# 9/1/2024


# Function to calculate profit
# Calculate profit based on revenue and expenses.
def calculate_profit(revenue, expenses):
    return revenue - expenses

# Main function to run the program
def main():
    revenue = 5000.0  # Example: Total revenue is $5000
    expenses = 3000.0  # Example: Total expenses are $3000
    profit = calculate_profit(revenue, expenses)
    print(f"Profit: ${profit:.2f}")

# Call the main function
if __name__ == "__main__":
    main()

