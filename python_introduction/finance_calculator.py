monthly_income = float(input("Enter your monthly income"))
monthly_expenses = float(input("Enter your monthly expenses"))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"your monthly_savings are $")
print(f"projected savings after one year, with interest, is: $ {int(annual_savings)}.")