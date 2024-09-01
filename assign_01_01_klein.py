# George Klein
# CBIS 4210
# Assignment 1.1
# 9/1/2024


# Function to calculate weekly pay
# Calculate total weekly pay based on hours worked and hourly rate.
def calculate_weekly_pay(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

# Main function to run the program
def main():
    hours_worked = 40  # Example: Employee works 40 hours a week
    hourly_rate = 20.0  # Example: Employee earns $20 per hour
    weekly_pay = calculate_weekly_pay(hours_worked, hourly_rate)
    print(f"Weekly Pay: ${weekly_pay:.2f}")

# Call the main function
if __name__ == "__main__":
    main()