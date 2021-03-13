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
    #[0, 0, 0],
    #[1, 1, 1],
    #[2, 2, 2],
    #[2, 2, 2, 2, 2, 2],

    #[1, 1, 1, 1, 1, 1],
    #[2, 1, 2, 2, 1, 2],
    #[2, 2, 1, 2, 2, 1]

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

def game():

    bot_score = 0
    user_score = 0

    print("Rock : 0 | Paper : 1 | Scissors : 2")

    i = 0
    while i in range(0, 100):
        try:
            user_move = int(input("Choose 0|1|2 \n"))
        except:
            print("No number selected!\n")
        else:
            bot_move = set_of_moves[i]

            if user_move not in [0, 1, 2, 5]:
                print("Choose from [0,1,2,5]")
                i = i - 1

            elif user_move in [0, 1, 2]:
                if user_move == 0 and bot_move == 1:
                    bot_score += 1
                    print("Bot wins!")
                elif user_move == 0 and bot_move == 2:
                    user_score += 1
                    print("You Win!")

                elif user_move == 1 and bot_move == 2:
                    bot_score += 1
                    print("Bot wins!")
                elif user_move == 1 and bot_move == 0:
                    user_score += 1
                    print("You Win!")

                elif user_move == 2 and bot_move == 0:
                    bot_score += 1
                    print("Bot wins!")
                elif user_move == 2 and bot_move == 1:
                    user_score += 1
                    print("You Win!")
                else:
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

game()
