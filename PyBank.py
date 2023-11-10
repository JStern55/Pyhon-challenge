import os
import csv

# Set the path to your CSV file
csv_file_path = 'C:\\users\\drjus\\PyBank\\Resources\\budget_data.csv'

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
monthly_changes = []
months = []

# Read the CSV file
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate through each row in the CSV
    for row in reader:
        # Extract data from the row
        date = row['Date']
        profit_loss = int(row['Profit/Losses'])
        
        # Calculate total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_loss
        
        # Calculate monthly change
        if total_months > 1:
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            months.append(date)
        
        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(monthly_changes) / (total_months - 1)

# Find the greatest increase and decrease in profits
greatest_increase = max(monthly_changes)
greatest_increase_month = months[monthly_changes.index(greatest_increase)]
greatest_decrease = min(monthly_changes)
greatest_decrease_month = months[monthly_changes.index(greatest_decrease)]

# Print the financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")