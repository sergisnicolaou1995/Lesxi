'''
keep score and count points
'''

nokozi_dict={ "J":2,
    "9":0,
    "A":11,
    "D":10,
    "K":4,
    "Q":3,
    "8":0,
    "7":0
       }

kozi_dict={ "J":20,
    "9":14,
    "A":11,
    "D":10,
    "K":4,
    "Q":3,
    "8":0,
    "7":0
       }


omada1=0
omada2=0


def kozia():
    a=0
    cards=input('kozia:')
    values1 = []
    for character in cards:
        for key, value in kozi_dict.items():
            if key == character:
                values1.append(value)
    a=sum(values1)+a
    return a



def oxi_kozia():
    b=0
    cards1=input('oxi kozia:')
    values2 = []
    for character in cards1:
        for key, value in nokozi_dict.items():
            if key == character:
                values2.append(value)
    b=sum(values2)+b
    return b



def anoigma_function():   
    anoigma=input('anoigma:')
    anoigma_int=int(anoigma)
    if anoigma_int>=80 and anoigma_int%10==0:
        anoigma_int=anoigma_int
        print('team anoigma:',anoigma_int)
    else:
        print('invalid anoigma')
        anoigma_function()
    return anoigma_int

        
    
def team_anoigma_function():
    team_anoigma=input('pia omada anoikse:')
    team_anoigma_int=int(team_anoigma)
    if team_anoigma_int==1 or team_anoigma_int==2:
        team_anoigma_int=team_anoigma_int
        print('pia omada anoikse:',team_anoigma_int)
    else:
        print('1 or 2 only')
        team_anoigma_function()
    return team_anoigma_int


    
def whose_points_function():
    whose_points=input('pias omadaa einai oi pontoi:')
    whose_points_int=int(whose_points)
    if whose_points_int==1 or whose_points_int==2:
        whose_points_int=whose_points_int
        print('pias omadas  einai oi pointoi:',whose_points_int)
    else:
        print('1 or 2 only')
        whose_points_function()
    return whose_points_int


        
while True:


    anoigma1=anoigma_function()
    team_anoigma1=team_anoigma_function()
    kapo=input('kapo:y/n')
    if kapo=='n':
        
        whose_points1=whose_points_function()
        c=kozia()
#("J9DAK8")
        d=oxi_kozia()
#("AD89KADJ7QK9QA")

        piso=input('piso: y/n')
        if piso=='y':
            e=c+d+10
        elif piso=='n':
            e=c+d

    elif kapo=='y':
        e=250

    klisto=input('klisto:y/n')
    if klisto=='y':
        anoixto=input('anoixto:y/n')
    elif klisto=='n':
        anoixto='n'
    
    

    dilosi1=input('team1 dilosi:')
    dilosi1_int=int(dilosi1)
    dilosi2=input('team2 dilosi:')
    dilosi2_int=int(dilosi2)

    

    if kapo=='y':
        
        if team_anoigma1==1:

            if anoigma1<=(e+dilosi1_int)and klisto=='N':                
                omada1=omada1+e+anoigma1+dilosi1_int
                omada2=omada2+dilosi2_int
            elif anoigma1>(e+dilosi1_int)and klisto=='N':
                omada1=omada1
                omada2=omada2+dilosi2_int+e+anoigma1+dilosi1_int

            elif anoigma1<=(e+dilosi1_int) and klisto=='Y' and anoixto=='N':
                omada1=omada1+(2*anoigma1)+e+dilosi1_int+dilosi2_int
                omada2=omada2
            elif anoigma1>(e+dilosi1_int) and klisto=='Y' and anoixto=='N':
                omada1=omada1
                omada2=omada2+(2*anoigma1)+e+dilosi1_int+dilosi2_int
                
            elif anoigma1<=(e+dilosi1_int) and klisto=='Y' and anoixto=='Y':
                omada1=omada1+(4*anoigma1)+e+dilosi1_int+dilosi2_int
                omada2=omada2
            elif anoigma1>(e+dilosi1_int) and klisto=='Y' and anoixto=='Y':
                omada2=omada2+(4*anoigma1)+e+dilosi1_int+dilosi2_int
                omada1=omada1

            
        elif team_anoigma1==2:
            
            if anoigma1<=(e+dilosi2_int) and klisto=='N':
                omada2=omada2+250+anoigma1+dilosi2_int
                omada1=omada1+dilosi1_int
            elif anoigma1>(e+dilosi2_int) and klisto=='N':
                omada2=omada2
                omada1=omada1+(2*anoigma1)+e+dilosi1_int+dilosi2_int
                
            elif anoigma1<=(e+dilosi2_int) and klisto=='Y' and anoixto=='N':
                omada2=omada2+(2*anoigma1)+250+dilosi1_int+dilosi2_int
                omada1=omada1
            elif anoigma1>(e+dilosi2_int) and klisto=='Y' and anoixto=='N':
                omada1=omada1+(2*anoigma1)+250+dilosi1_int+dilosi2_int
                omada2=omada2

            elif anoigma1<=(e+dilosi2_int) and klisto=='Y' and anoixto=='Y':
                omada2=omada2+(4*anoigma1)+250+dilosi1_int+dilosi2_int
                omada1=omada1
            elif anoigma1>(e+dilosi2_int) and klisto=='Y' and anoixto=='Y':
                omada1=omada1+(4*anoigma1)+250+dilosi1_int+dilosi2_int
                omada2=omada2            


        
    elif kapo=='n':

            
        if team_anoigma1==1 and whose_points1==1:
            #print('e1',e)   
            if anoigma1<=(e+dilosi1_int)and klisto=='N': 
                omada1=omada1+e+anoigma1+dilosi1_int
                omada2=omada2+(162-e)+dilosi2_int
                

            elif anoigma1>(e+dilosi1_int)and klisto=='N':
                omada1=omada1+0
                omada2=omada2+162+anoigma1+dilosi1_int+dilosi2_int

              
            elif anoigma1<=(e+dilosi1_int) and klisto=='Y'and anoixto=='N':
                omada2=omada2
                omada1=omada1+(2*anoigma1)+162+dilosi1_int+dilosi2_int

            elif anoigma1>(e+dilosi1_int) and klisto=='Y'and anoixto=='N':
                omada1=omada1
                omada2=omada2+(2*anoigma1)+162+dilosi1_int+dilosi2_int

            elif anoigma1<=(e+dilosi1_int) and klisto=='Y'and anoixto=='Y':
                omada2=omada2
                omada1=omada1+(4*anoigma1)+162+dilosi1_int+dilosi2_int

            elif anoigma1>(e+dilosi1_int) and klisto=='Y'and anoixto=='Y':
                omada1=omada1
                omada2=omada2+(4*anoigma1)+162+dilosi1_int+dilosi2_int

            

                

        elif team_anoigma1==2 and whose_points1==2:
            #print('e2',e)
            
            if anoigma1<=(e+dilosi2_int)and klisto=='N':       
                omada2=omada2+e+anoigma1+dilosi2_int
                omada1=omada1+(162-e)+dilosi1_int
                

            elif anoigma1>(e+dilosi2_int)and klisto=='N':
                omada2=omada2+0
                omada1=omada1+162+anoigma1+dilosi1_int+dilosi2_int

            elif anoigma1<=(e+dilosi2_int)and klisto=='Y' and anoixto=='N':
                omada1=omada1
                omada2=omada2+(2*anoigma1)+162+dilosi1_int+dilosi2_int

            elif anoigma1>(e+dilosi2_int)and klisto=='Y' and anoixto=='N':
                omada2=omada2
                omada1=omada1+(2*anoigma1)+162+dilosi1_int+dilosi2_int

            elif anoigma1<=(e+dilosi2_int)and klisto=='Y' and anoixto=='Y':
                omada1=omada1
                omada2=omada2+(4*anoigma1)+162+dilosi1_int+dilosi2_int

            elif anoigma1>(e+dilosi2_int)and klisto=='Y' and anoixto=='Y':
                omada2=omada2
                omada1=omada1+(4*anoigma1)+162+dilosi1_int+dilosi2_int


        elif team_anoigma1==1 and whose_points1==2:
            
            #print('e3',e)
            if anoigma1<=((162-e)+dilosi1_int)and klisto=='N':    
                omada1=omada1+(162-e)+anoigma1+dilosi1_int
                omada2=omada2+e+dilosi2_int            

            elif anoigma1>((162-e)+dilosi1_int)and klisto=='N':
                omada1=omada1+0
                omada2=omada2+162+anoigma1+dilosi1_int+dilosi2_int

            elif anoigma1<=((162-e)+dilosi1_int)and klisto=='Y' and anoixto=='N':
                omada2=omada2
                omada1=omada1+162+(2*anoigma1)+dilosi1_int+dilosi2_int

            elif anoigma1>((162-e)+dilosi1_int)and klisto=='Y' and anoixto=='N':
                omada1=omada1
                omada2=omada2+162+(2*anoigma1)+dilosi1_int+dilosi2_int

            elif anoigma1<=((162-e)+dilosi1_int)and klisto=='Y' and anoixto=='Y':
                omada2=omada2
                omada1=omada1+162+(4*anoigma1)+dilosi1_int+dilosi2_int

            elif anoigma1>((162-e)+dilosi1_int)and klisto=='Y' and anoixto=='Y':
                omada1=omada1
                omada2=omada2+162+(4*anoigma1)+dilosi1_int+dilosi2_int
        
            
                


        elif team_anoigma1==2 and whose_points1==1:
            #print('e4',e)
            if anoigma1<=((162-e)+dilosi2_int)and klisto=='N':      
                omada2=omada2+(162-e)+anoigma1+dilosi2_int
                omada1=omada1+e+dilosi1_int
                

            elif anoigma1>((162-e)+dilosi2_int)and klisto=='N':
                omada2=omada2+0/10
                omada1=omada1+162+anoigma1+dilosi1_int+dilosi2_int

            elif anoigma1<=((162-e)+dilosi2_int)and klisto=='Y' and anoixto=='N':
                omada1=omada1
                omada2=omada2+162+(2*anoigma1)+dilosi1_int+dilosi2_int

            elif anoigma1>((162-e)+dilosi2_int)and klisto=='Y'and anoixto=='N':
                omada2=omada2
                omada1=omada1+162+(2*anoigma1)+dilosi1_int+dilosi2_int

            elif anoigma1<=((162-e)+dilosi2_int)and klisto=='Y' and anoixto=='Y':
                omada1=omada1
                omada2=omada2+162+(4*anoigma1)+dilosi1_int+dilosi2_int

            elif anoigma1>((162-e)+dilosi2_int)and klisto=='Y'and anoixto=='Y':
                omada2=omada2
                omada1=omada1+162+(4*anoigma1)+dilosi1_int+dilosi2_int



    print('omada1',round(omada1))
    print('omada2',round(omada2))

    if omada1>3001:
        print('omada1 wins')
        break
    elif omada2>3001:
        print('omada2 wins')
        break


