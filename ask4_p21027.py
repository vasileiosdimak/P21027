import random
countp1 = 0
countp2 = 0
countdraw = 0
for i in range (100):
    print("new game")
    print("p1 starts the game")
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1>21:
        print("P2 wins!")
    else:
        print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            countp1 +=1
            print("P1 wins!")
        elif sum2>sum1:
            print("P2 wins!")
            countp2 +=1
        else:
            countdraw +=1
            print("draw!")
print("Me tyxaio moirasma ta statistika einai:")
print(f'o paiktis 1 kerdise {countp1} fores')
print(f'o paiktis 2 kerdise {countp2} fores')
print(f'eixame isopalia {countdraw} fores')
countp1 = 0
countp2 = 0
countdraw = 0
for i in range (100):
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    flag1 = True
    while sum1<16:
        sum1 = 0
        while (flag1):
            for i in range (51):
                if xartia[i][0] == 10 or xartia[i][0] == "K" or xartia[i][0] == "J" or xartia[i][0] == "Q":
                    player1.append(xartia.pop(i))
                    flag1 = False
                    break
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
    if sum1<21:
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            flag2 = True
            while (flag2):
                for i in range (51):
                    if xartia[i][0] != 10 or xartia[i][0] != "K" or xartia[i][0] != "J" or xartia[i][0] != "Q":
                        player2.append(xartia.pop(i))
                        flag2 = False
                        break
            player2.append(xartia.pop())
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
        if sum2>21:
            sum2=0
        if sum1>sum2:
            countp1 +=1
        elif sum2>sum1:
            countp2 +=1
        else:
            countdraw +=1
print("Me <<peiragmeno>> moirasma ta statistika einai:")
print(f'o paiktis 1 kerdise {countp1} fores')
print(f'o paiktis 2 kerdise {countp2} fores')
print(f'eixame isopalia {countdraw} fores')