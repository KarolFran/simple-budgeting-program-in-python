budget = float(input("Enter your budget: "))
while True:
    spending = float(input("Enter your spending amount: "))
    budget -= spending
    print("Budget after spendings is:",budget)
    