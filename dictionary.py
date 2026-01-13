books = {"python": 10.00, 
         "java": 12.00,
         "scala": 4.10,
         "data modeling": 7.00,
         "snowflake": 6.50,
         "sql": 3.29,
         "dbt": 4.99,
         "cloud": 5.99,
         "power bi": 2.50}

total = 0
cart = []

print("_______LIST OF BOOKS_______________")
for book, price in books.items():
    print(f"{book:20}: {price:.2f}")

while True:
    choice = input("Pick the book you want(q to quit): ").lower().strip()
    if choice == "q":
        break
    elif books.get(choice) is not None:
        cart.append(choice)
    else:
        print("The book is not available")


print("______YOUR_ORDERS__________")
for items in cart:
    print(items, end=" ")
    total+=books.get(items)
print()
print(f"Your total is: ${total:.2f}")


