#I think my og bank software might have been deleted, so let me speedrun
import _tkinter

#this is the welcome message
def welcome():
    print("Hello. Welcome to [Bank Name]!\n We're happy to help you.")
    print("Please obey the law, or consequences will come, so act accordingly.")

welcome()

#asks the user if they have used this bank before or not and determines what to do depending on their
#answer
def userType():
    input("First thing's first, are you a returning user or a new user?")

#The protocol for new users
def newUser():
    print("We're happy to have you join us.")
    username = input("Please enter your name.\n")
    print("Welcome, {username}! Please wait while we generate your ID...")

#the protocol for existing users
def oldUser():
    print("Welcome back.")
    iID = int(input("Please input your user ID.\n"))
    iPin = int(input("Please input your pin.\n"))