import os
def updateScore(player):
    for a in range(0, 20, 2):
        if(scores[int(player+1)][int(a/2)] == None):
            try:
                if(scores[int(player)][a] == 10):
                    if(scores[int(player)][a+2] == 10):
                        if(scores[int(player)][a+4] != None):
                            if(a == 0):
                                scores[int(player+1)][0] = 20+scores[int(player)][4]
                            else:
                                scores[int(player+1)][int(a/2)] = scores[int(player+1)][int((a/2)-1)]+20+scores[int(player)][a+4]
                    elif(scores[int(player)][a+2] != None):
                        if(a == 0):
                            scores[int(player+1)][0] = 10+scores[int(player)][2]+scores[int(player)][3]
                        else:
                            scores[int(player+1)][int(a/2)] = scores[int(player+1)][int((a/2)-1)]+10+scores[int(player)][a+2]+scores[int(player)][a+3]
                elif((scores[int(player)][a]+scores[int(player)][a+1]) == 10):
                    if(scores[int(player)][a+2] != None):
                        if(a == 0):
                            scores[int(player+1)][0] = 10+scores[int(player)][2]
                        else:
                            scores[int(player+1)][int(a/2)] = scores[int(player+1)][int((a/2)-1)]+10+scores[int(player)][a+2]
                else:
                    if(a == 0):
                        scores[int(player+1)][0] = scores[int(player)][0]+scores[int(player)][1]
                    else:
                        scores[int(player+1)][int(a/2)] = scores[int(player+1)][int((a/2)-1)]+scores[int(player)][a]+scores[int(player)][a+1]
            except:
                break
def rollCheck(roll, player):
    pins = ""
    try:
        pins = int(input("Roll "+str(roll)+": How many pins did you knock down?\n"))
    except:
        print("", end="")
    while((type(pins) != int) or (pins < 0) or (pins > 10) or ((roll == 2) and (pins+scores[int(2*player)][-1] > 10))):
        try:
            print("Invalid input! Please enter a number from 0 to "+str(10-scores[int(2*player)][-1])+":")
        except:
            print("Invalid input! Please enter a number from 0 to 10:")
        try:
            pins = int(input(""))
        except:
            continue
    return pins
def drawScoreboard(players):
    os.system('cls')
    for a in range(players):
        print("+-----------+"+10*"---+---+---+")
        print("|           |", end="")
        for b in range(0, 20, 2):
            if(b < 18):
                try:
                    if(scores[2*a][b] == 10):
                        print("   | X |   |", end="")
                    elif(scores[2*a][b] == 0):
                        if(scores[2*a][b+1] == 10):
                            print("   | - | / |", end="")
                        elif(scores[2*a][b+1] == 0):
                            print("   | - | - |", end="")
                        else:
                            print("   | - | "+str(scores[2*a][b+1])+" |", end="")
                    else:
                        if(scores[2*a][b]+scores[2*a][b+1] == 10):
                            print("   | "+str(scores[2*a][b])+" | / |", end="")
                        elif(scores[2*a][b+1] == 0):
                            print("   | "+str(scores[2*a][b])+" | - |", end="")
                        else:
                            print("   | "+str(scores[2*a][b])+" | "+str(scores[2*a][b+1])+" |", end="")
                except IndexError:
                    print("   |   |   |", end="")
            else:
                try:
                    if(scores[2*a][b] == 10):
                        if(scores[2*a][b+2] == 10):
                            if(scores[2*a][b+4] == 10):
                                print(" X | X | X |")
                            elif(scores[2*a][b+4] == 0):
                                print(" X | X | - |")
                            else:
                                print(" X | X | "+str(scores[2*a][b+4])+" |")
                        elif(scores[2*a][b+2] == 0):
                            if(scores[2*a][b+3] == 10):
                                print(" X | - | / |")
                            elif(scores[2*a][b+3] == 0):
                                print(" X | - | - |")
                            else:
                                print(" X | - | "+str(scores[2*a][b+3])+" |")
                        else:
                            if(scores[2*a][b+3] == 0):
                                print(" X | "+str(scores[2*a][b+2])+" | - |")
                            elif(scores[2*a][b+2]+scores[2*a][b+3] == 10):
                                print(" X | "+str(scores[2*a][b+2])+" | / |")
                            else:
                                print(" X | "+str(scores[2*a][b+2])+" | "+str(scores[2*a][b+3])+" |")
                    elif(scores[2*a][b] == 0):
                        if(scores[2*a][b+1] == 10):
                            if(scores[2*a][b+2] == 10):
                                print(" - | / | X |")
                            elif(scores[2*a][b+2] == 0):
                                print(" - | / | - |")
                            else:
                                print(" - | / | "+str(scores[2*a][b+2])+" |")
                        elif(scores[2*a][b+1] == 0):
                            print(" - | - |   |")
                        else:
                            print(" - | "+str(scores[2*a][b+1])+" |   |")
                    else:
                        if(scores[2*a][b]+scores[2*a][b+1] == 10):
                            if(scores[2*a][b+2] == 10):
                                print(" "+str(scores[2*a][b])+" | / | X |")
                            elif(scores[2*a][b+2] == 0):
                                print(" "+str(scores[2*a][b])+" | / | - |")
                            else:
                                print(" "+str(scores[2*a][b])+" | / | "+str(scores[2*a][b+2])+" |")
                        else:
                            print(" "+str(scores[2*a][b])+" | "+str(scores[2*a][b+1])+" |   |")
                except IndexError:
                    print("   |   |   |")
        print("|    P "+str(a+1)+"    |"+9*"   +---+---+"+"---+---+---+")
        print("|"+11*"           |")
        print("|           |", end="")
        for b in range(10):
            if(scores[(2*a)+1][b] != None):
                if(scores[(2*a)+1][b] < 10):
                    print("      "+str(scores[(2*a)+1][b])+"    |", end="")
                elif(scores[(2*a)+1][b] < 100):
                    print("     "+str(scores[(2*a)+1][b])+"    |", end="")
                else:
                    print("    "+str(scores[(2*a)+1][b])+"    |", end="")
            else:
                print("           |", end="")
        print("")
    print("+"+11*"-----------+")
scores = []
players = ""
try:
    players = int(input("\nHow many people are bowling (1-9)? "))
except:
    print("Invalid input! Please enter a number from 1-9: ", end="")
    while((type(players) != int) or (players < 0) or (players > 9)):
        try:
            players = int(input(""))
        except:
            print("Invalid input! Please enter a number from 1-9: ", end="")
for a in range(2*players):
    scores.append([])
for a in range(0, 2*players, 2):
    for b in range(10):
        scores[a+1].append(None)
for a in range(10):
    for b in range(0, 2*players, 2):
        drawScoreboard(players)
        print("\nPlayer "+str(int((b/2)+1))+" - Frame "+str(a+1)+":\n")
        print("Enter a number from 0 to 10 for how many pins you knocked down.\nEnter a 0 if you crossed the foul line.\n")
        pins = rollCheck(1, (b/2))
        scores[b].append(pins)
        if(pins != 10):
            pins = rollCheck(2, (b/2))
            scores[b].append(pins)
        else:
            scores[b].append(0)
        if(a == 9):
            if(scores[b][-1] == 0):
                pins = rollCheck(2, (b/2))
                scores[b].append(pins)
                if(pins != 10):
                    pins = rollCheck(3, (b/2))
                    scores[b].append(pins)
                else:
                    scores[b].append(0)
                    pins = rollCheck(3, (b/2))
                    scores[b].append(pins)
                    if(pins == 10):
                        scores[b].append(0)
            elif(pins+scores[b][-1] == 10):
                pins = rollCheck(3, (b/2))
                scores[b].append(pins)
        updateScore(b)
drawScoreboard(players)
print("")