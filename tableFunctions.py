from checkOrCreateData import checkOrCreateData

# Createing table data to pass through printTable()


def createTable(appData):
    tp = [["TOTAL", ":", str(appData['total'])]]
    types = appData['types'].split('/')
    # Loop for creating a data stucture (list of lists) to
    # provide printTable() fucntion with an argument
    for i in types:
        ts = []
        ts.append(i.upper())
        ts.append(":")
        ts.append(str(appData[i]))
        tp.append(ts)
    return list(zip(*tp))

# Function to prompt the user data in a presentable format


def printTable(table):
    colWidths = [0] * len(table)
    mainListLen = len(table)
    listOfListLen = len(table[0])
    for i in range(mainListLen):
        for x in table[i]:
            if (colWidths[i] < len(x)):
                colWidths[i] = len(x)
    for i in range(listOfListLen):
        for x in range(mainListLen):
            print(table[x][i].rjust(colWidths[x]), end=" ")
        print()
