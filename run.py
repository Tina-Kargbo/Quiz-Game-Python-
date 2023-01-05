
QuizPlay = input("Hello there! Would you like to take the quiz? yes or no? ")

if QuizPlay.lower() == "yes":
    print("Great, Let's play!")
elif QuizPlay.lower() == "no":
    quit()
else:
    print("This input is not valid. Please answer yes or no as a valid input.")


#code was taken from python CI lesson, "What are input/output operations?"
username = input("What is your name please?: ") 
print("Hello " + username + "! You will have 5 questions to answer. Try to answer as many questions as you can correctly to test your level of knowledge on the subject matter.")