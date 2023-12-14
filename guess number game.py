import random
def guessnumber():
    print("="*50)
    print("="*10,"WELCOME TO MY GUESS NUMBER GAME","="*10)
    print("="*50)
    y=int(input("enter a range"))    
    computer=random.randint(1,20)
    m,n=0,0
    while True:
        me=int(input("enter a number:"))
        if me==computer:
            print(computer)
            print("you won")
            m+=1
            print("ur score",m,":",n,"computer score")
        else:
            n+=1    
            print("awnnnn you loose try again later")
            print("ur score",m,":",n,"computer score")
guessnumber()      
        