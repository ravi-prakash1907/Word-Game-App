#   complete
file = 'winners.txt'

def readItWhole():
    try:
        fh = open(file, 'r')
        print("Winners\' List:\n\n")
        for eachWinner in fh:
            print(eachWinner)
        fh.close()
    except FileNotFoundError:
        print("List is empty!")

def readTopN(n):
    if n>10:
        n=10
    if retSize()<=10:
        readItWhole()
    else:
        i = 0
        try:
            fh = open(file, 'r')
            print("Recent Winners:\n\n")
            for eachWinner in fh:
                print(eachWinner)
                i+=1
                if i==n:
                    break
            fh.close()
        except FileNotFoundError:
            print("List is empty!")

# may be enhenced so that only new entries can be written rather then rewriting whole data after reading it
def win_update(newName):
    newName = newName+"\n"
    temp = [newName]
    try:
        fh = open(file, 'r+')    # 'r+w'
        for eachWinner in fh:
            temp.append(eachWinner)
            if len(temp) == 15:
                break
        fh.close()
    except FileNotFoundError:
        fh = open(file, 'w+')
        fh.close()

    fh = open(file, 'w+')
    fh.writelines(temp)
    fh.close()

def retSize():
    size = 0
    try:
        fh = open(file, 'r')
        for eachWinner in fh:
            size += 1
        fh.close()
        return size
    except FileNotFoundError:
        return size
