
import random

RED="\033[91m";GREEN="\033[92m";YELLOW="\033[93m";BLUE="\033[94m";CYAN="\033[96m";RESET="\033[0m"

snake={32:9,66:26,77:37,93:73,96:76,99:2}
ladder={3:43,16:45,34:67,49:92}

def cell(n,p1,p2):
    if n==p1==p2:return "🤝"
    if n==p1:return "🟢"
    if n==p2:return "🔵"
    if n in snake:return RED+"🐍"+RESET
    if n in ladder:return GREEN+"🪜"+RESET
    return f"{n:02}"

def board(p1,p2):
    print(CYAN+"\n========== 🐍 SNAKE & LADDER BOARD 🪜 ==========\n"+RESET)
    rows=[]
    nums=list(range(100,0,-1))
    idx=0
    for r in range(10):
        row=nums[idx:idx+10]
        idx+=10
        if r%2==1: row=row[::-1]
        print(" | ".join(f"{cell(x,p1,p2):^4}" for x in row))
        print("-"*68)

turn=1
p1=p2=0
print(CYAN+"🎮 WELCOME TO SNAKE & LADDER 🎮"+RESET)
board(p1,p2)

while p1<100 and p2<100:
    if turn%2==0:
        print(GREEN+"\n🟢 Hirva's Turn"+RESET)
        input("Press Enter 🎲 ")
        d=random.randint(1,6)
        print("🎲",d)
        if p1+d<=100:p1+=d
        if p1 in ladder:
            print("🪜 Ladder!")
            p1=ladder[p1]
        elif p1 in snake:
            print("🐍 Snake!")
            p1=snake[p1]
    else:
        print(BLUE+"\n🔵 Kartavya's Turn"+RESET)
        input("Press Enter 🎲 ")
        d=random.randint(1,6)
        print("🎲",d)
        if p2+d<=100:p2+=d
        if p2 in ladder:
            print("🪜 Ladder!")
            p2=ladder[p2]
        elif p2 in snake:
            print("🐍 Snake!")
            p2=snake[p2]
    print(f"\n📊 Hirva:{p1}   Kartavya:{p2}")
    board(p1,p2)
    turn+=1

print(GREEN+"🏆 Hirva Wins!" if p1>=100 else BLUE+"🏆 Kartavya Wins!",RESET)
