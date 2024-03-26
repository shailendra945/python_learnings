weekly_expenses = {"Sunday": 100, "Monday": 150, "Tuesday": 200,
                   "Wednesday": 90, "Thursday": 40, "Friday": 150, "Saturday": 200}
print("Weekly expense details :")
print(weekly_expenses)
print("1. get monday's expense ")
print(weekly_expenses["Monday"])
print("2. get total weekly expense")
print(sum(weekly_expenses.values()))
print("3.print all keys")
print(weekly_expenses.keys())
print(dir(dict))
print(type(weekly_expenses))