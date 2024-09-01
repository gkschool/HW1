# George Klein
# CBIS 4210
# Assignment 1.1
# 9/1/2024


# Function to calculate discounted price
# Calculate discounted price based on original price and discount percentage.
def calculate_discounted_price(original_price, discount_percentage):
    discount_amount = original_price * (discount_percentage / 100)
    return original_price - discount_amount

# Main function to run the program
def main():
    original_price = 100.0  # Example: Original price of the product is $100
    discount_percentage = 10  # Example: 10% discount is offered
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    print(f"Discounted Price: ${discounted_price:.2f}")

# Call the main function
if __name__ == "__main__":
    main()

