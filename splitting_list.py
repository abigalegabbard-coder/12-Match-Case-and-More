import random
import time

mystr = "This is a sentence about the hobgoblin Jace"
list_of_words = mystr.split() #if we specify nothing, it will spilt on " "
print(list_of_words)
list_of_words[-1] = "Mykyta"
print(list_of_words)
mystr = " ".join(list_of_words)
print(mystr)
# Simulated csv (comma seperated values)
str2 = "name,type,strength,health"
p1 = "zach,ork,5,10"
p2 = "issac,loot goblin,2,6"
headers = str2.split(",")
headers = p1.split(",")
headers = p2.split(",")
p1list= p1.split(",")
p2list= p2.split(",")

# Iterate through p1list with index and value (with enumerate)
for idx, val in enumerate(p1list):
    print(f"{headers[idx]}: {val}")

for idx, val in enumerate(p2list):
    print(f"{headers[idx]}: {val}")

playerlists= [p1list, p2list]
p1list.append(0)
p2list.append(0)
print(f"It's the big battle of {p1list[0]} the {p1list[1]} vs {p2list[0]} the {p2list[1]}!")
input("Press enter to continue!")
for i in range(5):
    print(f"Round {i+1}")
    choice = random.randint(0,2)
    outcomes = []
    if choice < 2:
        attacker = playerlists[choice]
        defender = playerlists[1-choice]
        outcomes.append(attacker[0])
        playerlists[choice][-1] += 1
        print(f"{attacker[0]} delivered {attacker[2]} damage to {defender[0]} and defeated them")
    else:
        outcomes.append("tie")
        print("It was a tie")
    time.sleep(3)

print(f"{p1list[0]} won {p1list[-1]} rounds")
print(f"{p2list[0]} won {p2list[-1]} rounds")
if p1list[-1] > p2list[-1]:
    print(p1list[0], "won!")
elif p2list[-1] > p1list[-1]:
    print(p1list[0], "won!")
else:
    print("It was a tie!")