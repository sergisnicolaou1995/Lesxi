'''
Simulate baseball game
'''
import numpy as np
import pandas as pd
pitches=["fb","off_speed"]
strike=["yes","no"]

swing_miss_rate_fastballs=[0.23,0.20,0.30,0.28,0.28,0.35,0.30,0.25,0.35]
swing_miss_rate_off_speed=[0.27,0.25,0.30,0.25,0.34,0.39,0.27,0.29,0.40]
babip=[0.3,0.298,0.312,0.280,0.280,0.270,0.250,0.250,0.230]


swinging=["yes","no"]
did_he_hit_it=["yes","no"]
in_play_outcome=["out","hit"]
outcome_in_play=["single","double","triple","home run"]

def pitch(balls,strikes):
    balls=balls
    strikes=strikes
    if balls==0 and strikes==0:
        pitch=np.random.choice(pitches,p=[0.7,0.3])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.7,0.3])
        else:
            for_strike=np.random.choice(strike,p=[0.5,0.5])
    
    elif balls==0 and strikes==1:
        pitch=np.random.choice(pitches,p=[0.6,0.4])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.6,0.4])
        else:
            for_strike=np.random.choice(strike,p=[0.35,0.65])

    elif balls==0 and strikes==2:
        pitch=np.random.choice(pitches,p=[0.25,0.75])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.25,0.75])
        else:
            for_strike=np.random.choice(strike,p=[0.15,0.85])

    elif balls==1 and strikes==0:
        pitch=np.random.choice(pitches,p=[0.7,0.3])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.7,0.3])
        else:
            for_strike=np.random.choice(strike,p=[0.4,0.6])

    elif balls==2 and strikes==0:
        pitch=np.random.choice(pitches,p=[0.75,0.25])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.75,0.25])
        else:
            for_strike=np.random.choice(strike,p=[0.55,0.45])

    elif balls==3 and strikes==0:
        pitch=np.random.choice(pitches,p=[0.8,0.2])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.8,0.2])
        else:
            for_strike=np.random.choice(strike,p=[0.35,0.65])

    elif balls==1 and strikes==1:
        pitch=np.random.choice(pitches,p=[0.5,0.5])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.65,0.35])
        else:
            for_strike=np.random.choice(strike,p=[0.35,0.65])

    elif balls==1 and strikes==2:
        pitch=np.random.choice(pitches,p=[0.4,0.6])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.6,0.4])
        else:
            for_strike=np.random.choice(strike,p=[0.35,0.65])

    elif balls==2 and strikes==1:
        pitch=np.random.choice(pitches,p=[0.7,0.3])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.7,0.3])
        else:
            for_strike=np.random.choice(strike,p=[0.4,0.6])

    elif balls==3 and strikes==1:
        pitch=np.random.choice(pitches,p=[0.75,0.25])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.75,0.25])
        else:
            for_strike=np.random.choice(strike,p=[0.65,0.35])

    elif balls==2 and strikes==2:
        pitch=np.random.choice(pitches,p=[0.65,0.35])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.7,0.3])
        else:
            for_strike=np.random.choice(strike,p=[0.55,0.45])

    elif balls==3 and strikes==2:
        pitch=np.random.choice(pitches,p=[0.5,0.5])
        if pitch=="fb":
            for_strike=np.random.choice(strike,p=[0.5,0.5])
        else:
            for_strike=np.random.choice(strike,p=[0.5,0.5])

    return pitch,for_strike

#p=pitch(3,2)
#print(p[0])
#print(p[1])

def pitch_input():
    type=input("pitch type: fb/off_speed")
    in_zone=input("for strike? yes/no")

    return str(type),str(in_zone)

#x=pitch_input()
#x[0]
#x[1]


    

def batter_swing(in_zone,strikes):

    if in_zone=="yes" and strikes<2:
        swing=np.random.choice(swinging,p=[0.5,0.5])

    elif in_zone=="yes" and strikes==2:
        swing=np.random.choice(swinging,p=[0.95,0.05])

    elif in_zone=="no" and strikes<2:
        swing=np.random.choice(swinging,p=[0.2,0.8])

    elif in_zone=="no" and strikes==2:
        swing=np.random.choice(swinging,p=[0.35,0.65])

    return swing

#batter_swing("yes",strikes=0)


def swing_outcome(babip,swing_miss_rate):

    sw=np.random.choice(did_he_hit_it,p=[(1-swing_miss_rate),swing_miss_rate])
    if sw=="yes":
       in_play=np.random.choice(in_play_outcome,p=[(1-babip),babip])
       if in_play=="out":
           result="out"
       elif in_play=="hit":
           result=np.random.choice(outcome_in_play,p=[0.45,0.35,0.05,0.15])
           
    else:
        result="swinging strike"
    
    return result

#swing_outcome(0.23,0.3)



def bases(hit,first_base,second_base,third_base):
    if hit=="single":
        first_base_new=1
        second_base_new=first_base
        third_base_new=second_base
        runs=third_base

    elif hit=="double":
        first_base_new=0
        second_base_new=1
        third_base_new=first_base
        runs=second_base+third_base

    elif hit=="triple":
        first_base_new=0
        second_base_new=0
        third_base_new=1
        runs=second_base+third_base+first_base

    elif hit=="home run":
        first_base_new=0
        second_base_new=0
        third_base_new=0
        runs=1+first_base+second_base+third_base


    return first_base_new,second_base_new,third_base_new,runs

#x=bases("home run",0,1,1)
#first=x[0]
#print("1st:",first)
#second=x[1]
#print("2nd:",second)
#third=x[2]
#print("3rd:",third)
#runs=x[3]
#print("runs:",runs)

def walk(first_base,second_base,third_base):
    if  first_base==0 and second_base==0 and third_base==0:
        first_base_new=1
        second_base_new=0
        third_base_new=0
        runs=0
    elif first_base==1 and second_base==0 and third_base==0:
        first_base_new=1
        second_base_new=1
        third_base_new=0
        runs=0
    elif first_base==0 and second_base==1 and third_base==0:
        first_base_new=1
        second_base_new=1
        third_base_new=0
        runs=0
    elif first_base==0 and second_base==0 and third_base==1:
        first_base_new=1
        second_base_new=0
        third_base_new=1
        runs=0
    elif first_base==1 and second_base==1 and third_base==0:
        first_base_new=1
        second_base_new=1
        third_base_new=1
        runs=0
    elif first_base==1 and second_base==0 and third_base==1:
        first_base_new=1
        second_base_new=1
        third_base_new=1
        runs=0
    elif first_base==0 and second_base==1 and third_base==1:
        first_base_new=1
        second_base_new=1
        third_base_new=1
        runs=0
    elif first_base==1 and second_base==1 and third_base==1:
        first_base_new=1
        second_base_new=1
        third_base_new=1
        runs=1

    return first_base_new,second_base_new,third_base_new,runs

#walk(0,1,1)


def half_inning(batter=1,bottom_ninth=False,away_team_runs=0,home_team_runs=0):
    batter_number=batter%9-1
    #print("batter number:",batter_number)
    batter_babip=babip[batter_number]
    batter_sw_miss_rate_fastballs=swing_miss_rate_fastballs[batter_number]
    batter_sw_miss_rate_off_speed=swing_miss_rate_off_speed[batter_number]

    balls=0
    strikes=0
    #print("balls",balls)
    #print("strikes",strikes)


    runs=0
    #print("runs",runs)

    hits=0
    #print("hits:",hits)

    walks=0
    #print("walks:",walks)

    outs=0
    #print("outs",outs)
    #runner on
    first_base=0
    #print("runner on first",first_base)
    second_base=0
   # print("runner on second",second_base)
    third_base=0
   # print("runner on third",third_base)
    events=[]

    if bottom_ninth==True:
        run_difference=away_team_runs-home_team_runs

    while(outs<3):
        #print("balls:",balls)
        #print("strikes:",strikes)
        #print("last batter outcome",events)
        #ptch=pitch_input()

        ptch=pitch(balls,strikes)
        
        
        print("--------------------------")
       # batter_sw_miss_rate=float
        if ptch[0]=="fb":
            batter_sw_miss_rate=batter_sw_miss_rate_fastballs
            print("pitch is fastball")
        elif ptch[0]=="off_speed":
            batter_sw_miss_rate=batter_sw_miss_rate_off_speed
            print("pitch is offspeed")



        bat_swing=batter_swing(ptch[1],strikes)
        if ptch[1]=="yes":
            print("in the zone")
        elif ptch[1]=="no":
            print("out of the zone")

        if bat_swing=="yes":
            print("batter did swing")
            sw_outcome=swing_outcome(batter_babip,batter_sw_miss_rate)
            if sw_outcome=="out":
                print("batter is out")
                outs=outs+1
                events.append(sw_outcome)
                batter_number=batter_number+1
            elif sw_outcome=="swinging strike":
                print("swinging strike")
                strikes=strikes+1

            else:
                print("batter hit a:",sw_outcome)
                events.append(sw_outcome)
                x=bases(sw_outcome,first_base,second_base,third_base)
                first_base=x[0]
                second_base=x[1]
                third_base=x[2]
                runs=x[3]+runs
                batter_number=batter_number+1
                hits=hits+1
                strikes=0
                balls=0

            if bottom_ninth==True:

                run_difference=run_difference-runs



        else:
            print("batter did not swing")
            #if pitch is strike
            if ptch[1]=="yes":
                strikes=strikes+1
            elif ptch[1]=="no":
                balls=balls+1

        if strikes==3:
            print("batter struck out")
            outs=outs+1
            batter_number=batter_number+1
            balls=0
            strikes=0
            events.append("strikeout")
        if balls==4:
            print("batter walked")
            batter_number=batter_number+1
            balls=0
            strikes=0
            walks=walks+1
            z=walk(first_base,second_base,third_base)
            first_base=z[0]
            second_base=z[1]
            third_base=z[2]
            runs=z[3]+runs
            events.append("walk")
            if bottom_ninth==True:

                run_difference=run_difference-runs


        if bottom_ninth==True:
            if run_difference<0:
                print("------------------------------")
                print("walk off")
                print("end of half inning")
                print("total runs in half inning:",runs)
                print("total hits in half inning:",hits)
                print("walks in half inning",walks)
                print("events this half inning",events)
                print("------------------------------")
                break
            #else:
             #   print("------------------------------")
              #  print("3 outs")
               # print("end of half inning")
               # print("total runs in half inning:",runs)
               # print("total hits in half inning:",hits)
               # print("walks in half inning",walks)
               # print("events this half inning",events)
               # print("------------------------------")
        
        if outs==3:
            print("------------------------------")
            print("3 outs")
            print("end of half inning")
            print("total runs in half inning:",runs)
            print("total hits in half inning:",hits)
            print("walks in half inning",walks)
            print("events this half inning",events)
            print("------------------------------")
            
    return runs,batter_number,hits,events

y=half_inning(bottom_ninth=True,away_team_runs=1,home_team_runs=1)
#y=half_inning()
#print(y[1])



first_batter_home=1
#runs_home=0
hits_home=0
total_runs_home=0
total_runs_away=0
first_batter_away=1
#runs_away=0
hits_away=0
col = {'team': ['away', 'home']} 
boxscore = pd.DataFrame(col)
boxscore["0"]=[0,0]
for i in range(1,30):
    #if (i >= 10) and (boxscore.sum(axis=1)[1] != boxscore.sum(axis=1)[0]):
     #   break


    print("away team bats")
    print("top of inning:",i)
    print("---------------")

    away=half_inning(first_batter_away)
    runs_away=away[0]
    total_runs_away=total_runs_away+runs_away
    #print("runs:",runs_away)
    hits_away=hits_away+away[2]
    #print("hits:",hits_away)
    first_batter_away=away[1]+1
    #print("events",away[3])

    if i<9:
        print("home team bats")
        print("bottom of inning:",i)
        print("---------------")

        home=half_inning(first_batter_home)
        runs_home=home[0]
        total_runs_home=total_runs_home+runs_home
        #print("runs:",runs_home)
        hits_home=hits_home+home[2]
        #print("hits:",hits_home)
        first_batter_home=home[1]+1
        #print("events",home[3])

        boxscore[str(i)]=[runs_away,runs_home]
    
    else:
        if (total_runs_home > total_runs_away):
            boxscore[str(i)] = [runs_away,'-']
            break

        else:
            print("home team bats")
            print("bottom of inning:",i)
            print("---------------")

            home=half_inning(first_batter_home,bottom_ninth=True,away_team_runs=total_runs_away,home_team_runs=total_runs_home)
            runs_home=home[0]
            total_runs_home=total_runs_home+runs_home
            #print("runs:",runs_home)
            hits_home=hits_home+home[2]
            #print("hits:",hits_home)
            first_batter_home=home[1]+1
            #print("events",home[3])

        boxscore[str(i)]=[runs_away,runs_home]
            

        if total_runs_home>total_runs_away:
            break
        elif total_runs_home<total_runs_away:
            break
        elif total_runs_home==total_runs_away:
            continue

    


 
boxscore=boxscore.drop("0",axis=1)
#boxscore["R"]=boxscore.sum(axis=1)
boxscore["R"]=[total_runs_away,total_runs_home]
boxscore["H"]=[hits_away,hits_home]
print(boxscore)

