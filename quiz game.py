questions = (
             "how amny elements are in the periodic table?: ",
             "how many bones are in the human body?: ",
             "which planet in the solar system is the hottest?: "
)

options = (("A. 115", "B. 117", "C. 118", "D. 119"), 
           ("A. 209", "B. 208", "C. 206", "D. 219"), 
           ("A. earth", "B. jupyter", "C. sun", "D. black hole"))

answers = ("C", "C", "C")
gusses = []
score = 0
question_number = 0


for question in questions:
    print("--------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess = input("Enter (A, B , C): ").upper()
    gusses.append(guess)
    if guess == answers[question_number]:
        score+=1
        print("CORRECT....!")
    else:
        print("INCORRECT...!")
        print(f"{answers[question_number]} is the correct answer..!")
    question_number+=1

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")