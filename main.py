import credits as c
import about as a       #using as statement
import winners as w
import play as p
import menu as m

# mainMenu

class mainMenu:
    """     docstring for mainMenu   """

    def __init__(self):
        self.menu = m.menu



    def getChoice(self, num):
        for item in self.menu:
            print("\n\t", item)
        num = int(input("\n\n* Enter your choice: "))
        return self.__checkChoice(num)


    def checkChoice(self, num):
        if (num == 1):
            return p.beg()
        elif (num == 2):
            a.details()
            return True
        elif (num == 3):
            c.developer()
            return True
        elif (num == 4):
            self.__winnerChoice()
            return True
        elif (num == 5):
            print("Exiting!!")
            return False
        else:
            print("Invalid choice!!")
            return False

    def winnerChoice(self):
        self.winMenu = ['Choose:-\n', '1) All Time Winners', '2) Recent Few']
        for item in self.winMenu:
            print("\n\t", item)
        self.c = int(input('\nYour choice: '))
        if self.c==1:
            w.readItWhole()
        elif self.c==2:
            self.temp = int(input('Specify no. of recent winners to be displayed(max 10): '))
            w.readTopN(self.temp)
        else:
            print("Invalid choice!!")

    __checkChoice = checkChoice
    __winnerChoice = winnerChoice
# ends class


# main function
def main():
    print("\n\nMAIN-MENU\n")
    begin = mainMenu()
    handler = True
    while handler:
        handler = begin.getChoice(0)
# ends main


main()
'''
if __name__ == '__main__':
    main()
'''



print("\n\nExecuted!!")
