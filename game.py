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
        toss = input("Enter your choice:")
        player1 = int(input("Enter a number"))
        player2 = random.randrange(1,7)
        print(player2)
        res = player1 + player2
        if((res % 2 == 0 and toss == "even") or (res % 2 != 0 and toss == "odd")):
                print("You have won the toss")
                print("Batting or Bowling")
                n = input("Enter your choice:")
                if(n == "batting"):
                        a = bat(target)
                        print("Score = ",a)
                        b = bowl(a)
                elif(n == "bowling"):
                        c = bowl(target)
                        print("Opponent Score = ",c)
                        d = bat(c)
        else:
                print("Opponent won the toss and choosed to bat first")
                e = bat(target)
                print("Score = ",e)
                f = bowl(e)

def bat(target):
        count = 0
        print("Target score:",target)
        print("Batting")
        for i in range(0,500):
                run = int(input("Your turn ->"))
                a = random.randrange(1,7)
                print("Opponent turn->",a)
                if(run != a and run <= 6):
                        count += run
                        print("Score->",count)
                elif(run == a):
                        print("Out")
                        break
                else:
                        print("Hey you can't hit more than 7 runs on a single strike")
        if(target != 0):
                if(count > target):
                        print("You're win")
                else:
                        print("You lose")
        else:
                target += count
                return target
def bowl(target):
        count = 0
        print("Target score:",target)
        print("Bowling")
        for i in range(0,500):
                run = int(input("Your turn ->"))
                a = random.randrange(1,7)   
                print("Opponent turn ->",a)
                if(run != a and run <= 6):
                        count += run
                        print("Score->",count)
                elif(run == a):
                        print("Out")
                        break
                else:
                        print("Enter less than 7")
        if(target != 0):
                if(target < count):
                        print("you're lose")
                else:
                        print("you're win")
        else:
                target += count       
                return target        
print("\t\t\t\t Hand Cricket")
menu = {1:("Start Game",play),
        2:("Rule",rule),
        3:"Quit game"}
for key,value in menu.items():
        print(key,"->",value[0])
choice = int(input("Enter your choice"))
if(choice == 1):
        menu[choice][1]()
elif(choice == 2):
        menu[choice][1]()
