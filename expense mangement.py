income = 0
expense = {}

def set_income():
    income
    try:
        val = float(input("\nEnter total montly income : "))
        if val < 0:
            print("Income cannot be negative")
        else:
            income = val
            print("Income successfully setted")
    except ValueError:
        print("Invalid input! Please enter a valid number")

def add_expense(category,amount):
    category = category.strip().title()
    if category in expense:
        expense[category] += amount
    else :
        expense[category] = amount

    print(f"Added {amount} to categoty '{category}'")

def get_summary():
    print("         EXPENSE & BUDGET SUMMARY        ")

    total_expense = sum(expense.values())
    remaining_balance = income - total_expense

    print(f"Total Income:     {income}")
    print(f"Total Expenses:   ${total_expense}")
    print(f"Remaining:        ${remaining_balance}")

    if not expense:
        print("No expenses recorded yet.")
    else:
        print("Category Breakdown:")
        for category, amount in expense.items():
            percentage = (amount / total_expense * 100) if total_expense > 0 else 0
            print(f" - {category:<15}: ${amount:>8,.2f} ({percentage:>5.1f}%)")

    if total_expense > income:
        overspent = total_expense - income
        print(f"WARNING: You have overspent by ${overspent}!")
    elif remaining_balance == 0 and income > 0:
        print("You have used 100% of your budget.")
    else:
        print("You are within your budget!")

def reset_data():
    income
    expense
    confirm = input("\nAre you sure you want to reset all data? (y/n): ").strip().lower()
    if confirm == 'y':
        income = 0
        expense.clear()
        print("All data reset")
    else:
        print("Action cancelled")

def main():
    while True:
        print("\n--- SMART BUDGET TRACKER ---")
        print("1. Set Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Reset Data")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            set_income()

        elif choice == '2':
            cat = input("Enter expense category (e.g., Food, Rent): ").strip()
            if not cat:
                print("Category name cannot be empty.")
                continue
            try:
                amt = float(input(f"Enter amount spent on '{cat}' ($): "))
                if amt <= 0:
                    print("Expense amount must be greater than 0.")
                else:
                    add_expense(cat, amt)
            except ValueError:
                print("Invalid input! Please enter a valid numerical amount.")

        elif choice == '3':
            get_summary()

        elif choice == '4':
            reset_data()

        elif choice == '5':
            print("\nThank you for using Smart Budget Tracker. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
