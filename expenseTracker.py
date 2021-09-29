budget = float(input("Enter your budget, press 0 to exit: "))
while True:
    spending = float(input("Enter your spending amount: "))
    budget -= spending
    if spending == 0:
        break
    print("Budget after spendings is:",budget)
