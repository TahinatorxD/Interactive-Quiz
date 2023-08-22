print("-------------------------------")
print("Welcome to the Interactive Quiz")
print("-------------------------------")

Score = 0

Start_Queue = input("Do you Want to start the Quiz? (Y/N)")
if Start_Queue == 'Y':
    print("-------> |Let The Quiz Begin| ")
# First Question
    Q1 = input("___________________________________________\n"
               "Q1 ---> When did the first World War start?\n"
               "A. 1987\n"
               "B. 1715\n"
               "C. 1914\n"
               "D. 2003\n"
               "Choose (A/B/C/D):- ")
    if Q1 == 'C':
        print("Correct Answer!!")
        print("The First World War also known as the Great war Began on 28, 1914.")
        Score += 1
        print("Your Current Score is: " + str(Score))
    else:
        print("Incorrect Answer!!")
        Score = Score
        print("Your Current Score is: " + str(Score))
# Second Question
    Q2 = input("_____________________________________________\n"
               "Q2 ---> When did the Great Depression Start? \n"
               "A. 1956\n"
               "B. 1929\n"
               "C. 2008\n"
               "D. 1917\n"
               "Choose (A/B/C/D):- ")
    if Q2 == 'B':
        print("Correct Answer!!")
        print("The longest and deepest downturn in the history of the modern industrial economy lasted more than a decade, beginning in 1929 and ending during World War II in 1941.")
        Score += 1
        print("Your Current Score is: " + str(Score))
    else:
        print("Incorrect Answer!!")
        Score = Score
        print("Your Current Score is: " + str(Score))
# Third Question
    Q3 = input("_____________________________________________\n"
               "Q3 ---> Who painted the Mona Lisa?\n"
               "A. Leonardo Da Vinci\n"
               "B. Pablo Picasso\n"
               "C. Edvard Munch\n"
               "D. Vincent Van Gogh\n"
               "Choose (A/B/C/D):- ")
    if Q3 == 'A':
        print("Correct Answer!!")
        print("The Mona Lisa painting is one of the most emblematic portraits in the history of art, where is located at the Louvre. Painted by Leonardo da Vinci in the 16th century")
        Score += 1
        print("Your Current Score is: " + str(Score))
    else:
        print("Incorrect Answer!!")
        Score = Score
        print("Your Current Score is: " + str(Score))
# Fourth Question
    Q4 = input("_____________________________________________\n"
               "Q4 ---> When did India gain independence from British rule?\n"
               "A. 1576\n"
               "B. 1928\n"
               "C. 1947\n"
               "D. 1976\n"
               "Choose (A/B/C/D):- ")
    if Q4 == 'C':
        print("Correct Answer!!")
        print("In August 1947, India and Pakistan win independence: “The Indian Independence Bill, which carves the independent nations of India and Pakistan out of the former Mogul Empire")
        Score += 1
        print("Your Current Score is: " + str(Score))
    else:
        print("Incorrect Answer!!")
        Score = Score
        print("Your Current Score is: " + str(Score))
# Fifth Question
    Q5 = input("_____________________________________________\n"
               "Q5 ---> Who was the Writer of Harry Potter Book Series?\n"
               "A. William Shakespeare\n"
               "B. J.K. Rowling\n"
               "C. George Orwell\n"
               "D. Jane Austen\n"
               "Choose (A/B/C/D):- ")
    if Q5 == 'B':
        print("Correct Answer!!")
        print("The writer of the Harry Potter book series is J.K. Rowling, whose full name is Joanne Rowling. ")
        Score += 1
        print("Your Current Score is: " + str(Score))
    else:
        print("Incorrect Answer!!")
        Score = Score
        print("Your Current Score is: " + str(Score))

    print(""
          "***********************************************\n"
          "Congratulations!! You have Finished The Test...")

    print("Your Final Score is:- " + str(Score))

    if Score == 0:
        print("You can only go up from here, GoodLuck for the Next time you try this quiz.")
    elif Score == 1:
        print("Well, that's one way to start! Keep going, the quiz won't quiz itself!")
    elif Score == 2:
        print("Two points! You're halfway to being twice as awesome!")
    elif Score == 3:
        print("Three cheers for your three points! You're doing better than a three-legged race!")
    elif Score == 4:
        print("Four-tunately, you're acing this! Just one more and you're a quiz whiz!")
    elif Score == 5:
        print("High five for the perfect score! You're nailing this quiz like a pro!")

    print("************************************************"
          "")

elif Start_Queue == 'N':
    print("There is still sometime before we start the Quiz.")