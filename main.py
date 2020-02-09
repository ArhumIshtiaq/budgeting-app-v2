#!/usr/bin/python
# Accounting.py - A simple command line based budgeting software with the
# ability to have data saved for, virtually, inifite amount of users.
#
# TO-DO:
# 1. Convert data storage to CSV
# 2. Add interface with Tkinter
# 3. Convert data storage to SQL
#

from checkOrCreateData import checkOrCreateData
from inputs import *
from miscFuncs import *
from progressBar import progressBar
from tableFunctions import printTable, createTable

printGreeting()
name, password = getNameAndPass()
user, appData = checkOrCreateData(name, password)


def main():
    printWait("Your current balance is Rs." + str(appData['total']))

    while True:
        cc, main, cclen = getCommand()
        if (main == "deposit"):
            user.deposit(int(cc[1]), appData)
        elif (main == "withdraw"):
            user.withdraw(int(cc[1]), appData)
        elif (cclen == 2):
            funcName(main, askAmount(), user, appData, cc)
        elif (cclen == 3):
            try:
                amount = int(cc[2])
                funcName(main, amount, user, appData, cc)
            except:
                funcName(main, askAmount(), user, appData, cc)
        elif (main == "summary"):
            printWait("Fetching summary...")
            progressBar()
            printTable(createTable(appData))
        elif (main == "exit" or main == "quit"):
            if (confirm("Are you sure? ") == True):
                printWait("\nThank you for using this budgeting software. See you next time, " + name[0].upper() + name[
                    1:] + ". Bye!")
                lastUser = name
                time.sleep(1)
                appData.close()
                quit()
        else:
            printWait("Sorry, I don't understand this command. Please try again.")


def returnAppData():
    return appData


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        printWait("Sorry, an error occured: " + str(error) + ".")
        printWait(" I am saving your work and quitting the program...")
        appData.close()
        quit()
