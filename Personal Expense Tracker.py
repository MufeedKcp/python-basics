expenses = [ 
    {"date": "2026-01-17", "item": "Coffee", "amount": 3.5}, 
    {"date": "2026-01-17", "item": "Book", "amount": 12.0},
 ]


def show_expenses(expenses_list):
    """
    show_expenses() is used to get dict's its key and values.

    """
    for value in expenses_list:
        print(f"date: {value['date']} | item: {value['item']} | amount: {value['amount']}")


print("-----Personal Expense Tracker------")
print("- - - - - - - - - - - - - - - - -")


while True:
    user_input = input("add expense/view expense/total expense/(q to exit): ").lower().strip()
    if user_input == "add expense":
        add_date = input("Enter the date: ")
        add_item = input("Enter the item: ")
        while True:
            try:
                add_amount = float(input("Enter the amount: "))
                if add_amount < 0:
                    print("You can't enter a negative number...!")
                    continue
                else:
                    break
            except ValueError:
                print("Enter a valid number")

        expenses.append({"date": add_date, "item": add_item, "amount": add_amount})
        print("Expense is succesesfully added to your tracker")

    elif user_input == "view expense":
        if len(expenses) == 0:
            print("No Expenses Found")
        else:
            show_expenses(expenses)

    elif user_input == "total expense":
        if len(expenses) == 0:
            print("expenses yet to be entered")
        elif len(expenses) >= 1:
            print("_____Your_expenses____")
            total = 0
            for value in expenses:
                print(f"{value['item']} - {value['amount']}")
                total+=value["amount"]
            print("__________________")
            print(f"Your Total expense is: ${total:.2f}")
            print(f"The total items is: {len(expenses)}")

    elif user_input == "q":
        break

