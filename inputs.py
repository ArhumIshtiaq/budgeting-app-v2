# Function to double-check user selection
def confirm(string):
    ans = input(string + "(y/n)\n").lower()
    if (ans == "y"):
        return True
    elif (ans == "n"):
        return False

# Asking for name and password to check against database


def getNameAndPass():
    name = input('Hi! What is your name?\nName:  ').lower()
    password = input('\nHi ' + name[0].upper() + name[1:] +
                     "! May I have you password as well?\nPassword:  ")
    return name, password

# Getting action to commit from user


def getCommand():
    command = str(
        input("\nWhat else would you like to do?\nCommand: ")).lower()
    cc = command.split(' ')
    main = cc[0]
    cclen = len(cc)
    return cc, main, cclen

# Asks for user to define amount, if not already done


def askAmount():
    amount = input("Amount?")
    while int(amount) <= 0 and amount.isnum():
        amount = int(
            input("Sorry, please enter an integer value greater than 0."))
    return int(amount)
