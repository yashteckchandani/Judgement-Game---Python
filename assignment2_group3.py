#-----------------------------------------------------------------------------
# PLEASE READ THE INSTRUCTIONS FILE FIRST OR ELSE YOU MAY FACE SOME ERRORS
#-----------------------------------------------------------------------------

import random

cards=["SA","SK","SQ","SJ","S10","S9","S8","S7","S6","S5","S4","S3","S2","HA","HK","HQ","HJ","H10","H9","H8","H7","H6","H5","H4","H3","H2","DA","DK","DQ","DJ","D10","D9","D8","D7","D6","D5","D4","D3","D2","CA","CK","CQ","CJ","C10","C9","C8","C7","C6","C5","C4","C3","C2"]

vals={"A":14,"K":13,"Q":12,"J":11,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}



def shuffle(user,deck_left):
    hand=random.sample(deck_left,13)
    user.extend(hand)
    for j in hand:
        deck_left.remove(j)





def call_win(user,user_cards,call_dict):
    if user=="player":
        win=int(input("How many turns can you potentially win : "))
        call_dict[user]=win
    else:
        win=0
        for m in user_cards:
            if m[1:] in ["A","K","Q","J"]:
                win=win+1
        call_dict[user]=win

              

users=["player","bot1","bot2","bot3"]



def make_arrange(users):
    arrange=[]
    arrange_users=[]
    s=random.randint(0,3)
    arrange.append(s)
    for m in range(3):
        if s!=3:
          s=s+1  
          arrange.append(s)
        elif s==3:
            s=0
            arrange.append(s)  
    for m in arrange:
        arrange_users.append(users[m])
    return arrange_users



def bot_ki_pehli_chal(user_cards):
    l=[]
    for m in user_cards:
        t=[]
        t.append(m)
        t.append(vals[m[1:]])
        t=tuple(t)
        l.append(t)
    l.sort(key=lambda x:x[1])
    return l[-1][0]

   





def bot_ki_baki_ki_chal(current_round,user,user_cards):
    possible_chances=[]
    possible_chances_to_choose_max=[]
    possible_chances_to_choose=[]
    chaal=""
    for m in current_round:
        if m[0]==current_round[0][0]:
            val_of_chance=vals[m[1:]]
            possible_chances.append(val_of_chance)
    max_val_of_chance=max(possible_chances)        
    for m in user_cards:
        if m[0]==current_round[0][0]:
            if vals[m[1:]]>max_val_of_chance:
                possible_chances_to_choose_max.append(m)
    if  len(possible_chances_to_choose_max)==0:
        for m in user_cards:
            if m[0]==current_round[0][0]:
                possible_chances_to_choose.append(m)
        if len(possible_chances_to_choose)!=0:
            l=[]
            for m in possible_chances_to_choose:
                t=[]
                t.append(m)
                t.append(vals[m[1:]])
                t=tuple(t)
                l.append(t)
            l.sort(key=lambda x:x[1])
            chaal = l[0][0]
            return chaal
        else:
            l=[]
            for m in user_cards:
                t=[]
                t.append(m)
                t.append(vals[m[1:]])
                t=tuple(t)
                l.append(t)
            l.sort(key=lambda x:x[1])
            chaal = l[0][0]
            return chaal           
    else:
        l=[]
        for m in possible_chances_to_choose_max:
            t=[]
            t.append(m)
            t.append(vals[m[1:]])
            t=tuple(t)
            l.append(t)
        l.sort(key=lambda x:x[1])
        chaal = l[-1][0]
        return chaal
def one_round(arrange_users):
        
        
        if arrange_users[0]!="player":
            x=bot_ki_pehli_chal(dict_link[arrange_users[0]])
            current_round_cards[arrange_users[0]]=x
            print(arrange_users[0],"=>",x)
            current_round.append(x)
            dict_link[arrange_users[0]].remove(x)
            for m in range(1,4):
                if arrange_users[m]=="player":
                    print("------------------------------------------------------------------------------")
                    print("YOUR CARDS==>>",player)
                    spade=[]
                    club=[]
                    diamond=[]
                    hearts=[]
                    for i in player:
                        if i[0]=="S":
                            spade.append(i)
                        elif i[0]=="C":
                            club.append(i)
                        elif i[0]=="D":
                            diamond.append(i)
                        elif i[0]=="H":
                            hearts.append(i)
                    print("cards in spades:",spade)
                    print("cards in clubs : ",club)
                    print("cards in diamond : ",diamond)
                    print("cards in hearts : ",hearts)
                    print("------------------------------------------------------------------------------")
                    n=input("Enter card :")
                    current_round_cards["player"]=n
                    current_round.append(n)
                    dict_link[arrange_users[m]].remove(n)
                else:
                    v=bot_ki_baki_ki_chal(current_round,arrange_users[m],dict_link[arrange_users[m]])
                    print(arrange_users[m],"=>",v)
                    current_round_cards[arrange_users[m]]=v
                    current_round.append(v)
                    dict_link[arrange_users[m]].remove(v)    

        else:
            print("------------------------------------------------------------------------------")
            print("YOUR CARDS==>>",player)
            spade=[]
            club=[]
            diamond=[]
            hearts=[]
            for m in player:
                if m[0]=="S":
                    spade.append(m)
                elif m[0]=="C":
                    club.append(m)
                elif m[0]=="D":
                    diamond.append(m)
                elif m[0]=="H":
                    hearts.append(m)
            print("cards in spades:",spade)
            print("cards in clubs : ",club)
            print("cards in diamond : ",diamond)
            print("cards in hearts : ",hearts)
            print("------------------------------------------------------------------------------")
            n=input("enter card :")
            current_round_cards["player"]=n
            current_round.append(n)
            player.remove(n)
            for m in range(1,4):
                    v=bot_ki_baki_ki_chal(current_round,arrange_users[m],dict_link[arrange_users[m]])
                    current_round_cards[arrange_users[m]]=v
                    print(arrange_users[m],"=>",v)
                    current_round.append(v)
                    dict_link[arrange_users[m]].remove(v) 

def win(current_cards,wins,current_round):
    suit=current_round[0][0]
    key=[]
    for m in current_cards.values():
        if m[0]!=suit:
            for i in current_cards.keys():
                if current_cards[i]==m:
                    key.append(i)
    for k in key:
        current_cards.pop(k)
    current_cards_list=current_cards.items()
    sort_list=[]
    for m in current_cards_list:
        k=list(m)
        k.append (vals[k[1][1:]])
        k=tuple(k)
        sort_list.append(k)
    sort_list.sort(key=lambda x:x[2])
    winner=sort_list[-1][0]
    for m in wins.keys():
        if m==winner:
            wins[m]=wins[m]+1
    return winner        


def calc_score(call,wins):
    call_list=call.items()
    score_list=[]
    score_dict={}
    for m in call_list:
        k=list(m)
        k.append(wins[k[0]])
        score_list.append(k)
    for m in score_list:
        if m[1]>m[2]:
            score=-10*m[1]
            score_dict[m[0]]=score
        else:
            score=(10*m[1])+(m[2]-m[1])
            score_dict[m[0]]=score
    return score_dict


def next_arrange(winner,sequence):
    out_sequence=[]
    out_sequence.append(winner)
    k=sequence.index(winner)
    if (0<k) and (k<3):
        for m in range(k+1,4):
            out_sequence.append(sequence[m])
        for m in range(0,k):
            out_sequence.append(sequence[m])
    elif k==3:
        for m in range(3):
            out_sequence.append(sequence[m])
    elif k==0:
        for m in range(1,4):
            out_sequence.append(sequence[m])
    return out_sequence      
                

def custom_input(file_name):
    f1=open(file_name,"r")
    #file_name="input.txt" we have taken\
    l=f1.readlines()
    bot1=l[0].split(" ")
    bot1=bot1[-1].split(",")
    bot1[-1]=bot1[-1][:-1]
    bot2=l[1].split(" ")
    bot2=bot2[-1].split(",")
    bot2[-1]=bot2[-1][:-1]
    bot3=l[2].split(" ")
    bot3=bot3[-1].split(",")
    bot3[-1]=bot3[-1][:-1]
    player=l[3].split(" ")
    player=player[-1].split(",")
    player[-1]=player[-1][:-1]
    sequence=l[4].split(" ")
    sequence=sequence[-1].split("->")
    t=(bot1,bot2,bot3,player,sequence)
    return t








wins_final={"player":0,"bot1":0,"bot2":0,"bot3":0}

while True:
    
    play_again=input("Countinue (Y/N) :")
    print()
    if play_again.upper()=="Y":
        player=[]
        bot1=[]
        bot2=[]
        bot3=[]
        sequence=[]
        n=input("do you want to play in random mode or enter text file mode (random/custom): ")
        print()
        if n.lower()=="random":
            cards_copy=["SA","SK","SQ","SJ","S10","S9","S8","S7","S6","S5","S4","S3","S2","HA","HK","HQ","HJ","H10","H9","H8","H7","H6","H5","H4","H3","H2","DA","DK","DQ","DJ","D10","D9","D8","D7","D6","D5","D4","D3","D2","CA","CK","CQ","CJ","C10","C9","C8","C7","C6","C5","C4","C3","C2"]
            shuffle(player,cards_copy)
            shuffle(bot1,cards_copy)
            shuffle(bot2,cards_copy)
            shuffle(bot3,cards_copy)
            print("cyclic order => user->bot1->bot2->bot3")
            sequence=["player","bot1","bot2","bot3"]
        else:
            file_name=input("enter file name: ")
           
            bot1,bot2,bot3,player,sequence=custom_input(file_name)
            
            print("cyclic order->",sequence)

        dict_link={"player":player,"bot1":bot1,"bot2":bot2,"bot3":bot3}
        current_round_cards={"player":"","bot1":"","bot2":"","bot3":""}



        wins={"player":0,"bot1":0,"bot2":0,"bot3":0}
        print()
        print("Your cards==>>",player)
        print()
        call={}
        call_win("player",player,call)
        call_win("bot1",bot1,call)
        call_win("bot2",bot2,call)
        call_win("bot3",bot3,call)
        print()
        print("The calls are :")
        print (call)
        print()
        
        arrange1=make_arrange(sequence)

        current_round=[]

        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 1  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        one_round(arrange1)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 2  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 3  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 4  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 5  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]    
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 6  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[] 
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 7  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]       
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 8  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]  
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 9  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]   
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 10  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]   
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 11  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]   
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 12  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        current_round=[]        
        print("\n$$$$$$$$$$$$$$$$$$$  ROUND 13  $$$$$$$$$$$$$$$$$$$\n")
        print("\n")
        arrange2=next_arrange(winner,sequence)
        one_round(arrange2)
        winner=win(current_round_cards,wins,current_round)
        print("------------------------------------------------------------------------------")
        print("winner==>>",winner)
        print("------------------------------------------------------------------------------")
        print("winning history",wins)
        print("------------------------------------------------------------------------------")
        
        
        print("final score")
        print("\n")
        win_score=calc_score(call,wins)
        win_round_list=[]
        for m in win_score.keys():
            k=[]
            k.append(m)
            k.append(win_score[m])
            k=tuple(k)
            print(k)
            win_round_list.append(k)
        win_round_list.sort(key=lambda x:x[1])
        winner_round=win_round_list[-1][0]

        print("\n")


        print(winner_round+" is the winner!!!!!!")
        print("\n")
        

        for m in win_score.keys():
            wins_final[m]=wins_final[m]+win_score[m]


    else:
        print()
        wins_final_list=[]
        for m in wins_final.keys():
            k=[]
            k.append(m)
            k.append(wins_final[m])
            k=tuple(k)
            #print(k)
            wins_final_list.append(k)
        win_round_list.sort(key=lambda x:x[1])
        print("TOTAL SCORES")
        for m in wins_final_list:
            print(m[0],"=>",m[1])
        wins_final_list.sort(key=lambda x:x[1])
        winner_series=wins_final_list[-1][0]
        print()
        print(winner_series+" wins the series")
        print("\n\n\n\n\n")
        break


        
