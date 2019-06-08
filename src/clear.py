from time import sleep

def clear():
    sleep(2)
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')
