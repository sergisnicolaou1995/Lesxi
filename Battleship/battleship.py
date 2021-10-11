'''
2x2 battleship
'''

import numpy as np
import random

def create_cord():
    x1=random.randint(1,5)
    y1=random.randint(1,5)

    if x1==5:
        x2=x1+random.randint(-1,0)
    elif x1==1:
        x2=x1+random.randint(0,1)
    elif x1!=5:
        x2=x1+random.randint(-1,1)
    
        
    if y1==5:
        y2=y1+random.randint(-1,0)
    elif y1==1:
        y2=y1+random.randint(0,1)
    elif y1!=5:
        y2=y1+random.randint(-1,1)


    if x2==x1 and y2==y1:
        create_cord()




    return(x1,y1,x2,y2)

def x_try():
    trial_x=int(input("guess x:"))
    print(trial_x)
    return trial_x
def y_try():
    trial_y=int(input("guess y:"))
    print(trial_y)
    return(trial_y)


x1_true,y1_true,x2_true,y2_true = create_cord()
if (x1_true == x2_true) and (y1_true == y2_true):
    x1_true,y1_true,x2_true,y2_true = create_cord()
# print(x1_true,y1_true,x2_true,y2_true)

def play(max_tries):
    grid = np.chararray((5,5), unicode=True)
    grid[:] = '-'
    c=0
    i=1
    while True:
        x1=x_try()
        y1=y_try()
        i=i+1
        if (x1==x1_true and y1==y1_true) or (x1==x2_true and y1==y2_true):
            grid[(4-(y1-1))][(x1-1)]="y"
            print("you hit the target")
            c=c+1 

        else:
            print("missed")
            grid[(4-(y1-1))][(x1-1)]="x"

        if c==2:
            print("you win")
            break
        if i==(max_tries + 1):
            print("you lose")
            break
        print(grid)
        #print("c=",c)    
        #print("i=",i)

play(10)

