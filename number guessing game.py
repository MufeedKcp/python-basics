# import random

# lowest_num = 1
# highest_num = 50
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True

# print(".......NUMBER GUESSING GAME......")
# print(f"Select a number between {lowest_num} and {highest_num}: ")

# while is_running:

#     guess = input("Enter your guess: ")
    
#     if guess.isdigit():
#         guess = int(guess)
#         guesses+=1

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#             print("Too low...Try again....")
#         elif guess > answer:
#             print("Too high.....Try again...")
#         else:
#             print(f"CORRECT...! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please select a number between {lowest_num} and {highest_num}")


import random

op_char = ("luffy", "sanji", "shanks", "garp", "roger", "rocks")

answer = random.choice(op_char)
chances = 5
is_running = True


print("_____Character Guessing Game_____")
print("----------------------------------")
print(f"Select a one piece character from {op_char} ")
while is_running:
    choice = input("Enter you guess: ").lower()
    chances-=1
    if chances == 0:
        print("You are used all your 5 chances...!")
        is_running = False
    if choice == answer:
        print(f"CORRECT....! The answer was {answer}")
        is_running = False
    else:
        print("Try again....")