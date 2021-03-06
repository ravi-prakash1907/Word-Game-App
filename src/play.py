#   incomplete

import winners as w
import clear as c
import menu as m

rules = "\nRULES:- \n\
        \n\t1) Players must have to enter the word within a fixed \
        \n\ttime-limit i.e. 30 seconds. \
        \n\t2) One who leaves game first would be considered defeated.\
        \n\t3) Player can accept defeat by entering \'*\' instead of \
        \n\tthe word. \
        \n\t4) All words must be in small letter.\n"

menuP = ["1) Main Menu", "2) Summary (of this game)", "3) Exit"]

def validateWord(player):
    global lastLetter
    global firstLetter
    global tempWord

    i = 1
    while True:
        if lastLetter!=firstLetter:
            if tempWord=='*':
                print("\nCongrats", player, "!! You won the Game!\n", end="")
                return False
            else:
                print("\nWord must begin with \'", lastLetter, "\'!")
                tempWord = input("Either enter right word, or accept your loss by entering \'*\': ")
                firstLetter = tempWord[0]
        if lastLetter == firstLetter:
            return True
        elif tempWord=='*':
            print("Congrats", player, "!! You won the Game!\n")
            return False
        i+=1
        if i==3:
            break

    if i==3:
        print("Sorry! You\'ve crossed limit.\nWinner is ", player, "!")
        return False

def max(a, b):
    x = len(a)
    if len(b) > x:
        x = len(b)
    return x

def summary(drawCheck):
    global wordsByP1
    global wordsByP2
    global p1
    global p2
    global turns
    winner=''
    flag=0
    i=0
    j=int(turns/2)-1
    print(j)

    print("\n\tWords entered respectivally:-\n\n", end="")

    if len(wordsByP2)!=0:
        for i in range (0, j):
            print("\tBy "+p1+": "+wordsByP1[i], end="")
            print("\tBy "+p2+": "+wordsByP2[i])
            flag=1
        if j==0 and flag==0:
            print("\tBy "+p1+": "+wordsByP1[i], end="")
            print("\tBy "+p2+": "+wordsByP2[i])
            i+=1
            winner=p2
            if turns%2!=0:
                print("\tBy "+p1+": "+wordsByP1[i])
                winner=p1
    else:
        print("\tBy "+p1+": "+wordsByP1[len(wordsByP1)-1])
        winner=p1

    if(flag==1):
        if len(wordsByP1)==len(wordsByP2):
            print("\tBy "+p1+": "+wordsByP1[len(wordsByP1)-1], end="")
            print("\tBy "+p2+": "+wordsByP2[len(wordsByP1)-1])
            winner=p2
        elif len(wordsByP2)==0:
            print("\tBy "+p1+": "+wordsByP1[len(wordsByP1)-1])
            winner=p1
        else:
            print("\tBy "+p2+": "+wordsByP2[len(wordsByP2)-1])
            winner=p2

    print("\n---------------\n\nResult:-\n", end="")

    print(turns)

    if drawCheck==turns:
        print("\tMatch Draw!")
    else:
        print("\tWinner is ", winner, "!")

    return m.postSummaryMenu()

def endGameMenu(drawCheck):
    print("\nMenu:-", end="")
    for item in menuP:
        print("\n\t", item)
    choice = int(input("\n\n* Enter your choice: "))

    if choice==1:
        print("\nMain Menu is called!")
        return True
    elif choice==2:
        return summary(drawCheck)
    else:
        print("\nExiting", end="")
        return False

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
    p1 = input("Name of first player: ")
    p2 = input("Name of second player:")
    turns = int(input("No. of words that each player\'d enter (max 40): "))
    #can varify that number is between 1 to 40 only
    turns *= 2
    disp = p1+"! Enter first word: "
    tempWord = input(disp)
    lastLetter = tempWord[-1]

    wordsByP1.append(tempWord)
    i=1
    while(i<turns):
        if i%2==0:
            disp1 = p1+"! Enter next word, starting with \'"+lastLetter+": "
            tempWord = input(disp1)
            firstLetter = tempWord[0]
            #timer
            if(validateWord(p2)):
                wordsByP1.append(tempWord)
                lastLetter = tempWord[-1]
            else:
                break
            i+=1
        else:
            disp2 = p2+"! Enter next word, starting with \'"+lastLetter+"\': "
            tempWord = input(disp2)
            firstLetter = tempWord[0]
            #timer

            if(validateWord(p1)):
                wordsByP2.append(tempWord)
                lastLetter = tempWord[-1]
            else:
                break
            i+=1

    print(i)
    print(turns)

    if i==turns:
        print("\n\nMatch Draw!!", end="")
    elif i%2==0:
        w.win_update(p2)
    else:
        w.win_update(p1)

    drawCheck = turns
    turns = i

    return endGameMenu(drawCheck)
