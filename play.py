#   incomplete

import winners as w
import clear as c

rules = "\nRULES:- \n\
        \n\t1) Players must have to enter the word within a fixed \
        \n\ttime-limit i.e. 30 seconds. \
        \n\t2) One who leaves game first would be considered defeated.\
        \n\t3) Player can accept defeat by entering \'*\' instead of \
        \n\tthe word. \
        \n\t4) All words must be in small letter.\n"

menu = ["1) Main Menu", "2) Summary (of this game)", "3) Exit"]

def validateWord(player):
    global lastLetter
    global firstLetter
    global tempWord

    i = 0
    while True:
        if lastLetter!=firstLetter:
            if tempWord=='*':
                print("\nCongrats", player, "!! You won the Game!\n")
                return False
            else:
                print("\nWord must begin with \'", lastLetter, "\'!")
                tempWord = input("\nEither enter right word, or accept your loss by entering \'*\': ")
                firstLetter = tempWord[0]
        if lastLetter == firstLetter:
            return True
        elif tempWord=='*':
            print("\nCongrats", player, "!! You won the Game!\n")
            return False
        i+=1
        if i==3:
            break

    if i==3:
        print("\nSorry! You\'ve crossed limit.\nWinner is ", player, "!")
        return False

def max(a, b):
    x = len(a)
    if len(b) > x:
        x = len(b)
    return x

def summery(drawCheck):
    global wordsByP1
    global wordsByP2
    global p1
    global p2
    turns = max(wordsByP1, wordsByP2)
    i=0

    print("\n\n\tWords entered respectivally:-\n\n", end="")
    for i in range (0, turns-1):
        print("\tBy "+p1+": "+wordsByP1[i], end="")
        print("\tBy "+p2+": "+wordsByP2[i])
    if len(wordsByP1)!=len(wordsByP2):
        if turns==len(wordsByP1):
            print("\tBy "+p1+": "+wordsByP1[i])
    else:
        print("\tBy "+p1+": "+wordsByP1[i], end="")
        print("\tBy "+p2+": "+wordsByP2[i])

    print("\n---------------\n\nResult:-\n", end="")
    if drawCheck==i:
        print("\tMatch Draw!")
    if i%2==0:
        print("\tWinner is ", p2, "!")
    else:
        print("\tWinner is ", p1, "!")

def endGameMenu(drawCheck):
    print("\nEnter your choice:-")
    for item in menu:
        print("\n\t", item)
    choice = int(input("\n\n* Enter your choice: "))

    if choice==1:
        print("\nMain Menu is called!")
    elif choice==2:
        summery(drawCheck-1)
    else:
        print("\nExiting")
        quit()

def beg():
    '''     variable decleration    '''
    global lastLetter
    global firstLetter
    global tempWord
    global wordsByP1
    global wordsByP2
    global p1
    global p2
    global turns

    turns = 0
    lastLetter = firstLetter = ''
    p1 = p2 = ''
    tempWord = ""
    wordsByP1 = []
    wordsByP2 = []


    '''     starting    '''


    print(rules)
    input("\n\t Hit to proceed.\n")

    print("\n\nLet\'s Begin:-\n")
    p1 = input("\nName of first player: ")
    p2 = input("\nName of second player:")
    turns = int(input("No. of words that each player\'d enter (max 40): "))
    #can varify that number is between 1 to 40 only
    turns *= 2
    disp = "\n"+p1+"\nEnter first word: "
    tempWord = input(disp)
    lastLetter = tempWord[-1]

    wordsByP1.append(tempWord)
    for i in range (1, turns):
        if i%2==0:
            disp1 = "\n"+p1+"! Enter next word, starting with \'"+lastLetter+": "
            tempWord = input(disp1)
            firstLetter = tempWord[0]
            #timer
            if(validateWord(p2)):
                wordsByP1.append(tempWord)
                lastLetter = tempWord[-1]
            else:
                break
        else:
            disp2 = "\n"+p2+"! Enter next word, starting with \'"+lastLetter+"\': "
            tempWord = input(disp2)
            firstLetter = tempWord[0]
            #timer

            if(validateWord(p1)):
                wordsByP2.append(tempWord)
                lastLetter = tempWord[-1]
            else:
                break

    if i==turns:
        print("\n\nMatch Draw!!")
    elif i%2==0:
        w.win_update(p2)
    else:
        w.win_update(p1)

    drawCheck = turns
    turns = i

    endGameMenu(drawCheck)
