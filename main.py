import pyautogui
from sys import argv
from json import load

once = '--once' in argv

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

w, h = pyautogui.size()

currentX, currentY = pyautogui.position()
def shallRun():
    global currentX, currentY

    x, y = pyautogui.position()
    r = currentX != x or currentY != y

    if r:
        currentX, currentY = x, y
    return r

def getWords():
    file = open('words.json')
    return load(file)

def selectWord(words: [(str, int)], done: [int], letters):
    selected = list(filter(lambda x: letters in x[0] and not x[1] in done, words))
    if not len(selected):
        return
    selection = selected[0]
    
    if bool(selection):
        done.append(selection[1])

    return selection[0]

def main():
    words = getWords()
    done = []
    
    while True:
        letters = input("Lettres :")

        selected = selectWord(words, done, letters)
        if not selected:
            continue

        print("🚀 ~ file: main.py:45 ~ selected:", selected)
        if not not selected:
            pyautogui.leftClick()
            pyautogui.typewrite(selected)
            pyautogui.press('enter')



if __name__ == '__main__':
    main()
