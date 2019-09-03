import random
target = 0
def rule():
        print("Play the game by entering any number less than or equal to 6")
        print("\t\t\tBatting rules")
        print("If the entered number and generated number is same,then you are out")
        print("Bowling rules")
        print("\t\t\tIf the entered number and generated number is same,then batsman is out")
def play():
        print("odd or even")
        toss = input()
        player1 = int(input())
        player2 = random.randrange(7)
        res = player1 + player2
        if((res % 2 == 0 and toss == "even") or (res % 2 != 0 and toss == "odd")):
                print("You have won the toss")
                a = player1()
                print(a)
def player1():
        print("Enter batting or bowling")
        choice = input()
        if(choice == "batting"):
                res = bat(target)
                return res
def bat(target):
        count = 0
        for i in range(0,500):
                run = int(input())
                if(run != random.range(7) and run <= 6):
                        print(count + run)
                elif(run == random.range(7)):
                        print("out")
                        break
                else:
                        print("Hey you can't hit 7 runs on a single strike")
                target += count
                return target
                        
print("\t\t\t\t Hand Cricket")
menu = {1:("Start Game",play),
        2:("Rule",rule),
        3:"Quit game"}
for key,value in menu.items():
        print(key,"->",value[0])
choice = int(input("Enter your choice:"))
if(choice == 1):
        menu[choice][1]()
elif(choice == 2):
        menu[choice][1]()
