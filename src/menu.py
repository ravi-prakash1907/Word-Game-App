menu = ["1) Play", "2) About", "3) Credit", "4) Winners", "5) Exit"]
menuS = ["1) Main Menu", "2) Exit"]

def postSummaryMenu():
    print("\nEnter your choice:-")
    for item in menuS:
        print("\n\t", item)
    choice = int(input("\n\n* Enter your choice: "))

    if choice==1:
        print("\nMain Menu is called!")
        return True
    elif choice==2:
        print("\nExiting")
        return False
