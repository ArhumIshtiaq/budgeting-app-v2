import os
import shelve
from inputs import confirm
from BudgetClass import Budget
from miscFuncs import printWait
from progressBar import progressBar


def checkOrCreateData(name, password):
    # Create shelve object while keeping nomenclature
    # to the specific user for easier access
    appData = shelve.open(('fad' + name))
    printWait("\nInitializing your account...")
    printWait("Retrieving any previous data, if any...")
    # Checking username against existing shelve data
    if (name in appData):
        progressBar(endText="Data found. Checking password...")
        # If username exists, then check password
        # against user-defined existing shelve data
        while (password != appData['password']):
            password = str(input("Wrong password. Try again!\nPassword: "))
        printWait("Password is correct! Logging in...")
        progressBar(endText="Success!")
        # Save the specific shelve object to a variable for
        # permanent data accessibility for the user session
        user = appData[name]
    else:
        progressBar(endText="No previous record found.")
        if (confirm("\nWould you like to create a new account?") == True):
            # Creating new user object using data provided
            # by user at script initialization
            user = Budget(name, password)
            # Saving customized class object to shelve object
            appData[user.user_name] = user
            printWait("Creating account...")
            progressBar(endText="Account created.")
        else:
            printWait("I will not create an account. Exiting program...")
            # Deleting data that this script may have unintentionally
            # created while checking for username against shelve data
            try:
                os.unlink(os.path.abspath(os.curdir) + "fad" + name + ".dir")
                pritn("Deleted .dir")
                os.unlink(os.path.abspath(os.curdir) + "fad" + name + ".bak")
                print("Deleted .bak")
                os.unlink(os.path.abspath(os.curdir) + "fad" + name + ".dat")
                print("Deleted .dat")
            except FileNotFoundError:
                print("Couldn't delete file.")
            quit()
    return user, appData
