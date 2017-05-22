import math
import random
#original work

#magic eight ball

#customer name
c_name = input("Hi, what's your name?\n")

answers1 = ["yes", "definitely", "possibly", "no"]
def converse(question):
    questions = question.split()
    if questions[0] == "nothing":
        exit
    elif "How" in questions:
        print("With a bit of elbow grease.")
        converse(input("What else can I predict for you, " + c_name + "?\n"))
    elif "die" in questions:
        print("In a moderate explosion.")
        converse(input("What else can I predict for you, " + c_name + "?\n"))
    else:
        print("Well, " + c_name + ", the answer to " + question + " is " + answers1[random.randrange(0, 3, 1)])
        converse(input("What else can I predict for you, " + c_name + "?\n"))

converse(input("What can I predict for you, " + c_name + "?\n"))
