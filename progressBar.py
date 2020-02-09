import time
from miscFuncs import printWait

# A visual representation of progress to help provide a better UX


def progressBar(marker="#", length=15, endText="Done!"):
    bar = "[]"
    progress = ""
    for i in range(length):
        progress += marker
        print(bar[0] + progress + " "*(length-1-i) +
              bar[1], flush=True, end="\r")
        time.sleep(0.1)
    printWait(endText.center(length+2), end="\n", flush=True)
