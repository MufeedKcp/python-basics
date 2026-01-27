tasks = [{"name": "Become solid intermediate in SQL", "status": True},
         {"name": "Python just enough for AE + DA", "status": False},
         {"name": "Master advanced SQL", "status": False},
         {"name": "Data modeling", "status": False}
]

def show_task():
        for num, line in enumerate(tasks, 1):
            if line["status"] == False:
                print(num, line["name"], "[   ]")
            elif line["status"] == True:
                print(num, line["name"], "[✓ ]")

while True:

    user_input = input("add task/view task/mark task as done/delete task/(q to quit): ").lower()

    if user_input == "add task":
        user = input("Enter the name of your task: ")
        tasks.append({"name": user, "status": False})

    elif user_input == "view task":
            show_task()
            
                
    elif user_input == "mark task as done":
            show_task()

            while True:
                try:
                    number = int(input("Which task number do you want to mark done?: "))
                    if number < 1 or number > len(tasks):
                        print("The number is out of range...!")
                        continue
                    else:
                        break
                except ValueError:
                    print("Enter a valid integer...!")            
            number-=1
            tasks[number].update({"status": True})
            show_task()

    elif user_input == "delete task":
        show_task()

        while True:
                try:
                    number1 = int(input("which task number?: "))
                    if number1 < 1 or number1 > len(tasks):
                        print("Enter a valid number....!")
                        continue
                    else:
                        break
                except ValueError:
                        print("Please enter a valid number...!")
        number1-=1
        tasks.pop(number1)

    elif user_input == "q":
        break
    
