def expense_calculator(expenses):
    total_expense = 0
    if type(expenses) == dict:
        total_expense = sum(expenses.values())
    else:
        total_expense = sum(expenses)

    return total_expense


expenses = [200, 400, 500, 150, 100, 45]
weekly_expenses = {"Sunday": 100, "Monday": 150, "Tuesday": 200,
                   "Wednesday": 90, "Thursday": 40, "Friday": 150, "Saturday": 200}
print("Calculate expenses :")
print(expense_calculator(expenses))
print(expense_calculator(weekly_expenses))

