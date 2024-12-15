monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly_savings are $ {int(monthly_savings)}")
print(f"projected savings after one year, with interest, is: $ {annual_savings}.")