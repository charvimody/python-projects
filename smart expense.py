expenses = []
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date: ")
    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }
    expenses.append(expense)
    print("Expense added successfully!")
def view_expenses():
    if len(expenses) == 0:
      print("No expenses found")
    return
    for i, e in enumerate(expenses, start=1):
         print(
        i,
        e["category"],
        "- ₹",
        e["amount"],
        "-",
        e["date"]
    )
def total_expense():
    total = sum(e["amount"] for e in expenses)
    print("Total = ₹", total)

def category_summary():
    summary = {}

    for e in expenses:
        cat = e["category"]

        if cat not in summary:
            summary[cat] = 0
            print("\nCategory Summary")

    for cat in summary:
        print(cat, "→ ₹", summary[cat])
while True:

    print("""
1 Add Expense
2 View Expenses
3 Total
4 Summary
5 Exit
""")

    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        category_summary()
    elif choice == "5":
        print ("goodbye")
        break
    else:
        print("Invalid choice. Please try again.")