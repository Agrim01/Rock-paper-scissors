import random as r
import numpy as n

intro = """
Welcome to Rock Paper Scissors game!
Have Fun!!
"""
print(intro)

choices = ["Rock", "Paper", "Scissors"]

patterns = [
    [0, 0],
    [1, 1],
    [2, 0, 2],
    [1, 2 ,2, 1, 2, 2],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1]
    # [0, 0, 0],
    # [1, 1, 1],
    # [2, 2, 2, 2, 2, 2],

    # [1, 1, 1, 1, 1, 1],
    # [2, 1, 2, 2, 1, 2],
    # [2, 2, 1, 2, 2, 1]

]

a = 0

while a < 50:
    if a == 0: 
        set1 = patterns[r.randint(0, 5)]
    else:
        set1 = set_of_moves
    set2 = patterns[r.randint(0, 5)]
    set_of_moves = n.concatenate((set1, set2))
    a += 1
    x = len(set_of_moves)
    if x >= 100:
        break

def registergame():

    bot_score = 0
    user_score = 0
    lst = []
    botlst = []
    print("Rock : 0 | Paper : 1 | Scissors : 2")
    
    

    i = 0
    while i in range(0, 20):
        try:
            user_move = int(input("Choose 0|1|2 \n"))
        except:
            print("No number selected!\n")
        else:
            bot_move = set_of_moves[i]
            
            if user_move not in [0, 1, 2, 5]:
                print("Choose from [0,1,2,5]")
                i = i - 1
                # print(i)

            elif user_move in [0, 1, 2]:
                if user_move == 0 and bot_move == 1:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 0 and bot_move == 2:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")

                elif user_move == 1 and bot_move == 2:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 1 and bot_move == 0:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")

                elif user_move == 2 and bot_move == 0:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 2 and bot_move == 1:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")
                else:
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Match Tied!")

            elif user_move == 5:
                exit0 = int(input("Sure to exit?(yes:1, no:0)"))

                if exit0 == 1:
                    break
                elif exit0 == 0:
                    continue

            i += 1

            if user_score + bot_score == 20:
                user_score_20 = user_score
                bot_score_20 = bot_score
            
    occurrence00=1
    occurrence01=1
    occurrence02=1
    occurrence10=1
    occurrence11=1
    occurrence12=1
    occurrence20=1
    occurrence21=1
    occurrence22=1

    occurrence000=0 
    occurrence001=0 
    occurrence002=0 
    occurrence010=0 
    occurrence011=0 
    occurrence012=0 
    occurrence020=0 
    occurrence021=0 
    occurrence022=0
    occurrence100=0 
    occurrence101=0 
    occurrence102=0 
    occurrence110=0 
    occurrence111=0 
    occurrence112=0 
    occurrence120=0 
    occurrence121=0 
    occurrence122=0
    occurrence200=0 
    occurrence201=0 
    occurrence202=0 
    occurrence210=0 
    occurrence211=0 
    occurrence212=0 
    occurrence220=0 
    occurrence221=0 
    occurrence222=0
    
           
    while i in range(20, 100):

        for j in range(len(lst)-1):
            if lst[j]==0 and botlst[j]==0:
                occurrence00+=1
            elif lst[j]==0 and botlst[j]==1:
                occurrence01+=1
            elif lst[j]==0 and botlst[j]==2:
                occurrence02+=1
            elif lst[j]==1 and botlst[j]==0:
                occurrence10+=1
            elif lst[j]==1 and botlst[j]==1:
                occurrence11+=1
            elif lst[j]==1 and botlst[j]==2:
                occurrence12+=1
            elif lst[j]==2 and botlst[j]==0:
                occurrence20+=1
            elif lst[j]==2 and botlst[j]==1:
                occurrence21+=1
            elif lst[j]==2 and botlst[j]==2:
                occurrence22+=1
        
        for j in range(len(lst)-1):
            if lst[j]==0 and botlst[j]==0 and lst[j+1]==0:
                occurrence000+=1
            elif lst[j]==0 and botlst[j]==0 and lst[j+1]==1:
                occurrence001+=1
            elif lst[j]==0 and botlst[j]==0 and lst[j+1]==2:
                occurrence002+=1
            elif lst[j]==0 and botlst[j]==1 and lst[j+1]==0:
                occurrence010+=1
            elif lst[j]==0 and botlst[j]==1 and lst[j+1]==1:
                occurrence011+=1
            elif lst[j]==0 and botlst[j]==1 and lst[j+1]==2:
                occurrence012+=1
            elif lst[j]==0 and botlst[j]==2 and lst[j+1]==0:
                occurrence020+=1
            elif lst[j]==0 and botlst[j]==2 and lst[j+1]==1:
                occurrence021+=1
            elif lst[j]==0 and botlst[j]==2 and lst[j+1]==2:
                occurrence022+=1
            elif lst[j]==1 and botlst[j]==0 and lst[j+1]==0:
                occurrence100+=1
            elif lst[j]==1 and botlst[j]==0 and lst[j+1]==1:
                occurrence101+=1
            elif lst[j]==1 and botlst[j]==0 and lst[j+1]==2:
                occurrence102+=1
            elif lst[j]==1 and botlst[j]==1 and lst[j+1]==0:
                occurrence110+=1
            elif lst[j]==1 and botlst[j]==1 and lst[j+1]==1:
                occurrence111+=1
            elif lst[j]==1 and botlst[j]==1 and lst[j+1]==2:
                occurrence112+=1
            elif lst[j]==1 and botlst[j]==2 and lst[j+1]==0:
                occurrence120+=1
            elif lst[j]==1 and botlst[j]==2 and lst[j+1]==1:
                occurrence121+=1
            elif lst[j]==1 and botlst[j]==2 and lst[j+1]==2:
                occurrence122+=1
            elif lst[j]==2 and botlst[j]==0 and lst[j+1]==0:
                occurrence200+=1
            elif lst[j]==2 and botlst[j]==0 and lst[j+1]==1:
                occurrence201+=1
            elif lst[j]==2 and botlst[j]==0 and lst[j+1]==2:
                occurrence202+=1
            elif lst[j]==2 and botlst[j]==1 and lst[j+1]==0:
                occurrence210+=1
            elif lst[j]==2 and botlst[j]==1 and lst[j+1]==1:
                occurrence211+=1
            elif lst[j]==2 and botlst[j]==1 and lst[j+1]==2:
                occurrence212+=1
            elif lst[j]==2 and botlst[j]==2 and lst[j+1]==0:
                occurrence220+=1
            elif lst[j]==2 and botlst[j]==2 and lst[j+1]==1:
                occurrence221+=1
            elif lst[j]==2 and botlst[j]==2 and lst[j+1]==2:
                occurrence222+=1
        
        p000 = float(occurrence000)/occurrence00
        p001 = float(occurrence001)/occurrence00
        p002 = float(occurrence002)/occurrence00
        p010 = float(occurrence010)/occurrence01
        p011 = float(occurrence011)/occurrence01
        p012 = float(occurrence012)/occurrence01
        p020 = float(occurrence020)/occurrence02
        p021 = float(occurrence021)/occurrence02
        p022 = float(occurrence022)/occurrence02
        p100 = float(occurrence100)/occurrence10
        p101 = float(occurrence101)/occurrence10
        p102 = float(occurrence102)/occurrence10
        p110 = float(occurrence110)/occurrence11
        p111 = float(occurrence111)/occurrence11
        p112 = float(occurrence112)/occurrence11
        p120 = float(occurrence120)/occurrence12
        p121 = float(occurrence121)/occurrence12
        p122 = float(occurrence122)/occurrence12
        p200 = float(occurrence200)/occurrence20
        p201 = float(occurrence201)/occurrence20
        p202 = float(occurrence202)/occurrence20
        p210 = float(occurrence210)/occurrence21
        p211 = float(occurrence211)/occurrence21
        p212 = float(occurrence212)/occurrence21
        p220 = float(occurrence220)/occurrence22
        p221 = float(occurrence221)/occurrence22
        p222 = float(occurrence222)/occurrence22

        j = len(lst)-1

        if lst[j]==0 and botlst[j]==0:
            x = max(p000,p001,p002)
            if x==p000:
                bot_move = 1 
            elif x==p001:
                bot_move = 2 
            elif x==p002:
                bot_move = 0

        if lst[j]==0 and botlst[j]==1:
            x = max(p010,p011,p012)
            if x==p010:
                bot_move = 1 
            elif x==p011:
                bot_move = 2 
            elif x==p012:
                bot_move = 0

        if lst[j]==0 and botlst[j]==2:
            x = max(p020,p021,p022)
            if x==p020:
                bot_move = 1 
            elif x==p021:
                bot_move = 2 
            elif x==p022:
                bot_move = 0

        if lst[j]==1 and botlst[j]==0:
            x = max(p100,p101,p102)
            if x==p100:
                bot_move = 1 
            elif x==p101:
                bot_move = 2 
            elif x==p102:
                bot_move = 0

        if lst[j]==1 and botlst[j]==1:
            x = max(p110,p111,p112)
            if x==p110:
                bot_move = 1 
            elif x==p111:
                bot_move = 2 
            elif x==p112:
                bot_move = 0

        if lst[j]==1 and botlst[j]==2:
            x = max(p120,p121,p122)
            if x==p120:
                bot_move = 1 
            elif x==p121:
                bot_move = 2 
            elif x==p122:
                bot_move = 0

        if lst[j]==2 and botlst[j]==0:
            x = max(p200,p201,p202)
            if x==p200:
                bot_move = 1 
            elif x==p201:
                bot_move = 2 
            elif x==p202:
                bot_move = 0

        if lst[j]==2 and botlst[j]==1:
            x = max(p210,p211,p212)
            if x==p210:
                bot_move = 1 
            elif x==p211:
                bot_move = 2 
            elif x==p212:
                bot_move = 0

        if lst[j]==2 and botlst[j]==2:
            x = max(p220,p221,p222)
            if x==p220:
                bot_move = 1 
            elif x==p221:
                bot_move = 2 
            elif x==p222:
                bot_move = 0
        

        try:
            user_move = int(input("Choose 0|1|2 \n"))
        except:
            print("No number selected\n")
        else:
            if user_move not in [0, 1, 2, 5]:
                print("Choose from [0,1,2,5]")
                i = i - 1
                # print(i)

            elif user_move in [0, 1, 2]:
                if user_move == 0 and bot_move == 1:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 0 and bot_move == 2:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")

                elif user_move == 1 and bot_move == 2:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 1 and bot_move == 0:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")

                elif user_move == 2 and bot_move == 0:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 2 and bot_move == 1:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")
                else:
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Match Tied!")

            elif user_move == 5:
                exit0 = int(input("Sure to exit?(yes:1, no:0)"))

                if exit0 == 1:
                    break
                elif exit0 == 0:
                    continue

            i += 1

            if user_score + bot_score == 20:
                user_score_20 = user_score
                bot_score_20 = bot_score

            if user_score + bot_score == 30:
                user_score_30 = user_score
                bot_score_30 = bot_score

    print("Your Score : " + str(user_score))
    print("Total untied matches : " + str(user_score + bot_score) )

    total_untied = user_score + bot_score

    print("Total matches: " + str(i))

    if i == 0:
        print("No match played!")
    elif total_untied == 0:
        print("Match Tied!")
    elif total_untied > 0:
        if bot_score > user_score:
            print("Bot is Winner!!")
            accuracy = (float(bot_score)/total_untied)*100
            print("Overall bot's accuracy was: " + str(accuracy) + "%")

            if total_untied >= 20:
                accuracy_20 = (float(bot_score_20)/20)*100
                print("Bot's accuracy when total untied matches were 20 was: " + str(accuracy_20) + "%")
                if total_untied >= 30:
                    accuracy_30 = (float(bot_score_30)/30)*100
                    print("Bot's accuracy when total untied matches were 30 was: " + str(accuracy_30) + "%")
        elif bot_score < user_score:
            print("You are Winner!!")
            accuracy = (float(bot_score)/total_untied)*100
            print("Overall bot's accuracy was: " + str(accuracy) + "%")

            if total_untied >= 20:
                accuracy_20 = (float(bot_score_20)/20)*100
                print("Bot's accuracy when total untied matches were 20 was: " + str(accuracy_20) + "%")
                if total_untied >= 30:
                    accuracy_30 = (float(bot_score_30)/30)*100
                    print("Bot's accuracy when total untied matches were 30 was: " + str(accuracy_30) + "%")
        else:
            print("Match Tied!!")
            print("Overall bot's accuracy was 50%")
            if total_untied >= 20:
                accuracy_20 = (float(bot_score_20)/20)*100
                print("Bot's accuracy when total untied matches were 20 was: " + str(accuracy_20) + "%")
                if total_untied >= 30:
                    accuracy_30 = (float(bot_score_30)/30)*100
                    print("Bot's accuracy when total untied matches were 30 was: " + str(accuracy_30) + "%")

    return lst, botlst

def logingame(lst, botlst):

    bot_score = 0
    user_score = 0

    i = len(lst)

    for b in range(len(lst)):
            if lst[b] == 0 and botlst[b] == 1:
                bot_score += 1
            elif lst[b] == 0 and botlst[b] == 2:
                user_score += 1

            elif lst[b] == 1 and botlst[b] == 2:
                bot_score += 1
            elif lst[b] == 1 and botlst[b] == 0:
                user_score += 1

            elif lst[b] == 2 and botlst[b] == 0:
                bot_score += 1
            elif lst[b] == 2 and botlst[b] == 1:
                user_score += 1

            if user_score + bot_score == 20:
                user_score_20 = user_score
                bot_score_20 = bot_score

            if user_score + bot_score == 30:
                user_score_30 = user_score
                bot_score_30 = bot_score

    occurrence00=1
    occurrence01=1
    occurrence02=1
    occurrence10=1
    occurrence11=1
    occurrence12=1
    occurrence20=1
    occurrence21=1
    occurrence22=1

    occurrence000=0 
    occurrence001=0 
    occurrence002=0 
    occurrence010=0 
    occurrence011=0 
    occurrence012=0 
    occurrence020=0 
    occurrence021=0 
    occurrence022=0
    occurrence100=0 
    occurrence101=0 
    occurrence102=0 
    occurrence110=0 
    occurrence111=0 
    occurrence112=0 
    occurrence120=0 
    occurrence121=0 
    occurrence122=0
    occurrence200=0 
    occurrence201=0 
    occurrence202=0 
    occurrence210=0 
    occurrence211=0 
    occurrence212=0 
    occurrence220=0 
    occurrence221=0 
    occurrence222=0
    
           
    while i in range(len(lst), 100):

        for j in range(len(lst)-1):
            if lst[j]==0 and botlst[j]==0:
                occurrence00+=1
            elif lst[j]==0 and botlst[j]==1:
                occurrence01+=1
            elif lst[j]==0 and botlst[j]==2:
                occurrence02+=1
            elif lst[j]==1 and botlst[j]==0:
                occurrence10+=1
            elif lst[j]==1 and botlst[j]==1:
                occurrence11+=1
            elif lst[j]==1 and botlst[j]==2:
                occurrence12+=1
            elif lst[j]==2 and botlst[j]==0:
                occurrence20+=1
            elif lst[j]==2 and botlst[j]==1:
                occurrence21+=1
            elif lst[j]==2 and botlst[j]==2:
                occurrence22+=1
        
        for j in range(len(lst)-1):
            if lst[j]==0 and botlst[j]==0 and lst[j+1]==0:
                occurrence000+=1
            elif lst[j]==0 and botlst[j]==0 and lst[j+1]==1:
                occurrence001+=1
            elif lst[j]==0 and botlst[j]==0 and lst[j+1]==2:
                occurrence002+=1
            elif lst[j]==0 and botlst[j]==1 and lst[j+1]==0:
                occurrence010+=1
            elif lst[j]==0 and botlst[j]==1 and lst[j+1]==1:
                occurrence011+=1
            elif lst[j]==0 and botlst[j]==1 and lst[j+1]==2:
                occurrence012+=1
            elif lst[j]==0 and botlst[j]==2 and lst[j+1]==0:
                occurrence020+=1
            elif lst[j]==0 and botlst[j]==2 and lst[j+1]==1:
                occurrence021+=1
            elif lst[j]==0 and botlst[j]==2 and lst[j+1]==2:
                occurrence022+=1
            elif lst[j]==1 and botlst[j]==0 and lst[j+1]==0:
                occurrence100+=1
            elif lst[j]==1 and botlst[j]==0 and lst[j+1]==1:
                occurrence101+=1
            elif lst[j]==1 and botlst[j]==0 and lst[j+1]==2:
                occurrence102+=1
            elif lst[j]==1 and botlst[j]==1 and lst[j+1]==0:
                occurrence110+=1
            elif lst[j]==1 and botlst[j]==1 and lst[j+1]==1:
                occurrence111+=1
            elif lst[j]==1 and botlst[j]==1 and lst[j+1]==2:
                occurrence112+=1
            elif lst[j]==1 and botlst[j]==2 and lst[j+1]==0:
                occurrence120+=1
            elif lst[j]==1 and botlst[j]==2 and lst[j+1]==1:
                occurrence121+=1
            elif lst[j]==1 and botlst[j]==2 and lst[j+1]==2:
                occurrence122+=1
            elif lst[j]==2 and botlst[j]==0 and lst[j+1]==0:
                occurrence200+=1
            elif lst[j]==2 and botlst[j]==0 and lst[j+1]==1:
                occurrence201+=1
            elif lst[j]==2 and botlst[j]==0 and lst[j+1]==2:
                occurrence202+=1
            elif lst[j]==2 and botlst[j]==1 and lst[j+1]==0:
                occurrence210+=1
            elif lst[j]==2 and botlst[j]==1 and lst[j+1]==1:
                occurrence211+=1
            elif lst[j]==2 and botlst[j]==1 and lst[j+1]==2:
                occurrence212+=1
            elif lst[j]==2 and botlst[j]==2 and lst[j+1]==0:
                occurrence220+=1
            elif lst[j]==2 and botlst[j]==2 and lst[j+1]==1:
                occurrence221+=1
            elif lst[j]==2 and botlst[j]==2 and lst[j+1]==2:
                occurrence222+=1
        
        p000 = float(occurrence000)/occurrence00
        p001 = float(occurrence001)/occurrence00
        p002 = float(occurrence002)/occurrence00
        p010 = float(occurrence010)/occurrence01
        p011 = float(occurrence011)/occurrence01
        p012 = float(occurrence012)/occurrence01
        p020 = float(occurrence020)/occurrence02
        p021 = float(occurrence021)/occurrence02
        p022 = float(occurrence022)/occurrence02
        p100 = float(occurrence100)/occurrence10
        p101 = float(occurrence101)/occurrence10
        p102 = float(occurrence102)/occurrence10
        p110 = float(occurrence110)/occurrence11
        p111 = float(occurrence111)/occurrence11
        p112 = float(occurrence112)/occurrence11
        p120 = float(occurrence120)/occurrence12
        p121 = float(occurrence121)/occurrence12
        p122 = float(occurrence122)/occurrence12
        p200 = float(occurrence200)/occurrence20
        p201 = float(occurrence201)/occurrence20
        p202 = float(occurrence202)/occurrence20
        p210 = float(occurrence210)/occurrence21
        p211 = float(occurrence211)/occurrence21
        p212 = float(occurrence212)/occurrence21
        p220 = float(occurrence220)/occurrence22
        p221 = float(occurrence221)/occurrence22
        p222 = float(occurrence222)/occurrence22

        j = len(lst)-1

        if lst[j]==0 and botlst[j]==0:
            x = max(p000,p001,p002)
            if x==p000:
                bot_move = 1 
            elif x==p001:
                bot_move = 2 
            elif x==p002:
                bot_move = 0

        if lst[j]==0 and botlst[j]==1:
            x = max(p010,p011,p012)
            if x==p010:
                bot_move = 1 
            elif x==p011:
                bot_move = 2 
            elif x==p012:
                bot_move = 0

        if lst[j]==0 and botlst[j]==2:
            x = max(p020,p021,p022)
            if x==p020:
                bot_move = 1 
            elif x==p021:
                bot_move = 2 
            elif x==p022:
                bot_move = 0

        if lst[j]==1 and botlst[j]==0:
            x = max(p100,p101,p102)
            if x==p100:
                bot_move = 1 
            elif x==p101:
                bot_move = 2 
            elif x==p102:
                bot_move = 0

        if lst[j]==1 and botlst[j]==1:
            x = max(p110,p111,p112)
            if x==p110:
                bot_move = 1 
            elif x==p111:
                bot_move = 2 
            elif x==p112:
                bot_move = 0

        if lst[j]==1 and botlst[j]==2:
            x = max(p120,p121,p122)
            if x==p120:
                bot_move = 1 
            elif x==p121:
                bot_move = 2 
            elif x==p122:
                bot_move = 0

        if lst[j]==2 and botlst[j]==0:
            x = max(p200,p201,p202)
            if x==p200:
                bot_move = 1 
            elif x==p201:
                bot_move = 2 
            elif x==p202:
                bot_move = 0

        if lst[j]==2 and botlst[j]==1:
            x = max(p210,p211,p212)
            if x==p210:
                bot_move = 1 
            elif x==p211:
                bot_move = 2 
            elif x==p212:
                bot_move = 0

        if lst[j]==2 and botlst[j]==2:
            x = max(p220,p221,p222)
            if x==p220:
                bot_move = 1 
            elif x==p221:
                bot_move = 2 
            elif x==p222:
                bot_move = 0
        

        try:
            user_move = int(input("Choose 0|1|2 \n"))
        except:
            print("No number selected\n")
        else:
            if user_move not in [0, 1, 2, 5]:
                print("Choose from [0,1,2,5]")
                i = i - 1
                # print(i)

            elif user_move in [0, 1, 2]:
                if user_move == 0 and bot_move == 1:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 0 and bot_move == 2:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")

                elif user_move == 1 and bot_move == 2:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 1 and bot_move == 0:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")

                elif user_move == 2 and bot_move == 0:
                    bot_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Bot wins!")
                elif user_move == 2 and bot_move == 1:
                    user_score += 1
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("You Win!")
                else:
                    lst.append(user_move)
                    botlst.append(bot_move)
                    print("Match Tied!")

            elif user_move == 5:
                exit0 = int(input("Sure to exit?(yes:1, no:0)"))

                if exit0 == 1:
                    break
                elif exit0 == 0:
                    continue

            i += 1

            if user_score + bot_score == 20:
                user_score_20 = user_score
                bot_score_20 = bot_score

            if user_score + bot_score == 30:
                user_score_30 = user_score
                bot_score_30 = bot_score

    print("Your Score : " + str(user_score))
    print("Total untied matches : " + str(user_score + bot_score) )

    total_untied = user_score + bot_score

    print("Total matches: " + str(i))

    if i == 0:
        print("No match played!")
    elif total_untied == 0:
        print("Match Tied!")
    elif total_untied > 0:
        if bot_score > user_score:
            print("Bot is Winner!!")
            accuracy = (float(bot_score)/total_untied)*100
            print("Overall bot's accuracy was: " + str(accuracy) + "%")

            if total_untied >= 20:
                accuracy_20 = (float(bot_score_20)/20)*100
                print("Bot's accuracy when total untied matches were 20 was: " + str(accuracy_20) + "%")
                if total_untied >= 30:
                    accuracy_30 = (float(bot_score_30)/30)*100
                    print("Bot's accuracy when total untied matches were 30 was: " + str(accuracy_30) + "%")
        elif bot_score < user_score:
            print("You are Winner!!")
            accuracy = (float(bot_score)/total_untied)*100
            print("Overall bot's accuracy was: " + str(accuracy) + "%")

            if total_untied >= 20:
                accuracy_20 = (float(bot_score_20)/20)*100
                print("Bot's accuracy when total untied matches were 20 was: " + str(accuracy_20) + "%")
                if total_untied >= 30:
                    accuracy_30 = (float(bot_score_30)/30)*100
                    print("Bot's accuracy when total untied matches were 30 was: " + str(accuracy_30) + "%")
        else:
            print("Match Tied!!")
            print("Overall bot's accuracy was 50%")
            if total_untied >= 20:
                accuracy_20 = (float(bot_score_20)/20)*100
                print("Bot's accuracy when total untied matches were 20 was: " + str(accuracy_20) + "%")
                if total_untied >= 30:
                    accuracy_30 = (float(bot_score_30)/30)*100
                    print("Bot's accuracy when total untied matches were 30 was: " + str(accuracy_30) + "%")

    return lst, botlst