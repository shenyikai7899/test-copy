#花旗骰
'''
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，
庄家胜；玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
'''
from random import *
    
def main():
    money = 1000
    count = 0
    while money >= 0:        
        bet = 100
        '''int(input('请输入你的赌注：'))'''
        money += gambl(bet)
        count +=1
        print(f'当前筹码为{money},赌博次数为{count}')
        if money <= 0:
            print('你输了')
            break
        elif money >= 2000:
            print('你赢了')
            break

def gambl(bet):
    count = 0
    while True: 
        points = rollDice()
        print(points)
        count += 1
        if count == 1:
            fristpoints = points
            print('第一次是',fristpoints)
        if (points == 7 or points == 11) and count ==1:
            print(f'玩家胜,一共摇了{count}次骰子')
            return bet
            
        elif (points == 2 or points == 3 or points == 12) and count == 1:
            print(f'庄家胜,一共摇了{count}次骰子')
            return -bet
           
        elif points == 7 and count >1:
            print(f'庄家胜,一共摇了{count}次骰子')
            return -bet
            
        elif points == fristpoints and count >1:
            print(f'玩家胜,一共摇了{count}次骰子')
            return bet
        

def rollDice():
    p = randint(1,6) + randint(1,6)
    return p

main()
