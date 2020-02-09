from miscFuncs import printWait
from progressBar import progressBar


class Budget():

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        self.types = []
        appData['user_name'] = user_name
        appData['password'] = password
        appData['total'] = 0

        """
        The following line of code is a workaround of the fact that shelve objects can not store dictionaries.
        I have programmed it so that all the types will be in a single string, seperated by the fron-slash(/).
        When the need arises, this program will split the string and use the resulting data accordingly.
        """
        appData['types'] = "/".join(self.types)

    def deposit(self, amount, appData):
        if amount > 0:
            appData['total'] += amount
            print("Depositing...")
            progressBar(endText="Deposit Succesful!")
            printWait("Your total balance now is Rs." + str(appData['total']))

    def withdraw(self, amount, appData):
        if (amount > appData['total']):
            print("Sorry, you do not have enough money!")
        else:
            appData['total'] -= amount
            print("Withdrawing...")
            progressBar(endText="Withdrawal Succesful!")
            printWait("Your total balance now is Rs." + str(appData['total']))

    def create(self, name, amount, appData):
        types = appData['types'].split('/')
        types.append(name)
        appData['types'] = "/".join(types)
        if (amount > appData['total']):
            print("Sorry, you do not have enough money to spend on this thing!")
        else:
            appData['total'] -= amount
            appData[name] = amount
            printWait("Your total balance now is Rs." + str(appData['total']))

    def add(self, type_, amount, appData):
        appData['total'] -= amount
        if appData[type_] > 0:
            appData[type_] += amount
        else:
            appData[type_] = 0
            appData[type_] += amount
        printWait("Your total balance now is Rs." + str(appData['total']))

    def remove(self, type_, amount, appData):
        if (amount > appData[type_]):
            print("Sorry, that's not possible!")
        elif (amount == appData[type_]):
            types.remove(type_)
            appData['types'] = "/".join(types)
        else:
            appData['total'] += amount
            appData[type_] -= amount
            print("Tranferring Rs." + str(amount) +
                  " back to your Total Balance...")
            progressBar(endText="Transfer Complete!")
            printWait("Your total balance now is Rs." + str(appData['total']))
