'''
kouppi: keep score and money
'''
import numpy as np
deck={1:"A",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"J",12:"Q",13:"K"}

cards=list(range(1,14))

players={1:"Sergis",2:"Demos",3:"Kotsios",4:"Giorgos"}

money={1:1000,2:1000,3:1000,4:1000}
pot=80
money[1]=money[1]-pot
money[2]=money[2]-pot
money[3]=money[3]-pot
money[4]=money[4]-pot

turn=1

while (True):
    if turn==5:
        turn=1  
    print("-------------------------------")
    print("player turn:",players[turn])
    print("player money:",money[turn])
    print("pot money:",pot)
    left=np.random.choice(cards)
    print("left:",deck[left])
    right=np.random.choice(cards)
    print("right:",deck[right])
    middle=np.random.choice(cards)


    if (abs(left-right)>2):

        choice=input("pass/bet/kouppi?")
        if choice=="p":
            print("middle",deck[middle])

        elif choice=="k":

            print("middle",deck[middle])
            if middle<max(left,right) and middle>min(left,right):
                money[turn]=money[turn]+pot
                pot=80
            else:
                money[turn]=money[turn]-pot
                pot=pot+pot
      
        else:
            print("middle",deck[middle])
            if middle<max(left,right) and middle>min(left,right):
                money[turn]=money[turn]+int(choice)
                pot=pot-int(choice)
            else:
                money[turn]=money[turn]-int(choice)
                pot=pot+int(choice)



        print("player money:",money[turn])
        turn=turn+1
    else:
        turn=turn+1



    #continue1=input("STOP GAME? y/n")
    #if continue1=="y":
     #   break





