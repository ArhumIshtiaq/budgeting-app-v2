import time

# A greeting to be printed at every initialization of the program


def printGreeting(width=80):
    print("*"*width)
    print("\n\n" + "Welcome to Arhum's Python Budgeting Script!".center(width) + "\n\n")
    print("*"*width)

# A prompt-and-wait function to reduce repetition of same lines of code


def printWait(string, timer=0.8, flush=True, end="\n"):
    print(string, flush=flush, end=end)
    time.sleep(timer)

# Name of the user specified action (when cclen > 1)


def funcName(main, amount, user, appData, cc):
    if (main == "create"):
        user.create(cc[1], amount, appData)
    elif (main == "add"):
        user.add(cc[1], amount, appData)
    elif (main == "remove"):
        user.remove(cc[1], amount, appData)
