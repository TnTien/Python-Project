#
#   Python: 3.9.5
#
#   Author: Tien Nguyen
#
#   Purpose:    The Tech Academy - Python Course, Creating our first program together.
#   Demonstrating how to pass variables from function to function
#   while producing a functional game.
#
#   Remember, function_name(variable) _means that we pass in the variable.
#   return variable _means that we are returning the variable
#   back to the calling function.


def start():
    fName = "Sarah"
    lName = "Connor"
    age = 28
    gender = "Female"
    get_info(fName, lName, age, gender)

def get_number():
    number = 12
    return number

def get_name():
    name = input("What is your name? ")
    return name

def get_info(fName, lName, age, gender):
    print("My name is {} {}. I am a {} year old {}.".format(fName, lName, age, gender))



if __name__ == "__main__":
    start()
