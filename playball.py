from random import random
def getinputs():#获得初始数据
    a=eval(input("请输入选手A的能力值0-1:"))
    b=eval(input("请输入选手B的能力值0-1:"))
    n=eval(input("模拟比赛的场数:"))
    return a,b,n
def simngames(n,probA,probB):#模拟n场比赛
    winsA,winsB=0,0
    for i in range(n):
        scoreA,scoreB=simOnegame(probA,probB)
        if scoreA>scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB
def gameover(a,b):
    return a==15 or b==15
def simOnegame(probA,probB):#模拟一场比赛
    scoreA,scoreB= 0 , 0
    serving ='A'
    while not gameover(scoreA,scoreB):
        if serving=='A': 
            if random() < probA:
                scoreA+=1
            else:
                serving='B'
        else:
            if random()<probB:
                scoreB+=1
            else:
                serving='A'
    return scoreA,scoreB
def printSummary(winsA,winsB):
    n=winsA+winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
def play_main():
    probA,probB,n=getinputs()
    winsA,winsB=simngames(n,probA,probB)
    printSummary(winsA,winsB)
if __name__=='_main_':
    play_main()
    