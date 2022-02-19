from pickle import FALSE
import random
from re import T
rounds = 0
for r in range (100):
    values=[0,1,2]
    box0 =[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    box1= [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    box2= [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    circles=[9,9,9]
    round_counter=0
    game_win = True
    while(game_win):
        round_counter +=1
        z=random.choice(list(values))
        #Επιλογη τυχαίου τετραγώνου στο αντιστοιχο κουτι , ανάλογα το μεγεθος του δακτυλιου
        cell = True
        while(cell):
            i=random.choice(list(values))
            j=random.choice(list(values))
            if z == 0 and box0[i][j] == -1:   
                box0[i][j] = 0
                print("epilogi mikrou daktyliou")
                cell= False
            elif z == 1 and box1[i][j] == -1:
                box1[i][j] = 0
                print("epilogi mesaiou dactyliou")
                cell= False
            elif z == 2 and box2[i][j] == -1 :
                box2[i][j] = 0
                print("epilogi megalou dactyliou")
                cell= False
        if round_counter >= 3:
            if z == 0:
                #Οριζοντια
                for i in range (2):
                    if box0[i][0] != -1:
                        if box0[i][1] == 0:
                            if box0[i][2] == 0:
                                game_win = False
                        elif box1[i][1] == 0:
                            if box2[i][2] == 0:
                                game_win = False
                #καθετα
                for j in range (2):
                    if box0[0][j] != -1:
                        if box0[1][j] == 0:
                            if box0[2][j] == 0: 
                                game_win = False
                        elif box1[i][1] == 0:
                            if box2[i][2] == 0:
                                game_win = False
                #διαγωνια
                    if box0[0][0] != -1:
                        if box0[1][1] == 0 :
                            if box0[2][2] == 0:
                                game_win = False
                        elif box1[1][1] == 0:
                            if box2[2][2] == 0:
                                game_win = False
                        elif box0[2][0] == 0:
                            if box0[1][1] == 0:
                                if box0[2][2] == 0:
                                    game_win = False
                            elif box1[1][1] == 0:
                                if box2[2][2] == 0:
                                    game_win = False
            elif z == 1:
                #Οριζοντια
                for i in range (2):
                    if box1[i][0] != -1:
                        if box1[i][1] == 0:
                            if box1[i][2] == 0:
                                game_win = False
                    if box0[i][0] == 0:
                        if box1[i][1] == 0:
                            if box2[i][2] == 0:
                                game_win = False
                #καθετα
                for j in range (2):
                    if box1[0][j] != -1:
                        if box1[1][j] == 0:
                            if box1[2][j] == 0: 
                                game_win = False
                    if box0[0][j] == 0:
                        if box1[1][j] == 0:
                            if box2[2][j] == 0:
                                game_win = False
                #διαγωνια
                    if box1[0][0] == 0:
                        if box1[1][1] == 0 :
                            if box1[2][2] == 0:
                                game_win = False
                    elif box1[2][0] == 0:
                        if box1[1][1] == 0 :
                            if box1[0][2] == 0:
                                game_win = False
                    if box0[0][0] == 0:
                        if box1[1][1] == 0:
                            if box2[2][2] == 0:
                                game_win = False
                    elif box0[2][0] == 0:
                        if box1[1][1] == 0:
                            if box2[0][2] == 0:
                                game_win = False
            else:
                #Οριζοντια
                for i in range (2):
                    if box2[i][0] == 0:
                        if box2[i][1] == 0:
                            if box2[i][2] == 0:
                                game_win = False
                    if box0[i][0] == 0:
                        if box1[i][1] == 0:
                            if box2[i][2] == 0:
                                game_win = False
                #καθετα
                for j in range (2):
                    if box2[0][j] == 0:
                        if box2[1][j] == 0:
                            if box2[2][j] == 0: 
                                game_win = False
                    if box0[0][j] == 0:
                        if box1[1][j] == 0:
                            if box2[2][j] == 0:
                                game_win = False
                #διαγωνια
                if box2[0][0] == 0 :
                    if box2[1][1] == 0:
                        if box2[2][2] == 0:
                            game_win = False
                elif box2[2][0] == 0:
                    if box2[1][1] == 0:
                        if box2[0][2] == 0:
                            game_win = False
                if box0[0][0] == 0:
                        if box1[1][1] == 0:
                            if box2[2][2] == 0:
                                game_win = False
                elif box0[2][0] == 0:
                    if box1[1][1] == 0:
                        if box2[0][2] == 0:
                            game_win = False
    rounds= rounds + round_counter   
print("mesos oros vimatwn gia ton termatismo kathe paixnidiou",rounds/100)
print("telos")            

            







   