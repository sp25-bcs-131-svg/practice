income = 0
expense = {}

def set_income():
    try:
        val = float(input("\nEnter total montly income : "))
        if val < 0:
            print("Income cannot be negative")
        else:
            income = val
            print("Income successfully setted")
    except ValueError:
        print("Invalid input! Please enter a valid number")

