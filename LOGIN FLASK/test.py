import random

die1, die2, die3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
print("Die 1: " + str(die1))
print("Die 2: " + str(die2))
print("Die 3: " + str(die3))


# implementation method 1
# this method uses the dictionary to map the values corresponding to the condition.
value = {(die1 == die2 and die2 == die3): "Three of a kind", (die1 == die2 or die2 == die3 or die1 == die3): "1Pair"}.get(True, "Better luck next time!")
print(value)

"""
# implementation method 2
# this is the usual else if ladder implementation of the above oneliner code
if(die1 == die2 and die2 == die3):
    print("Three of a kind")
elif(die1 == die2 or die2 == die3 or die1 == die3):
    print("1Pair")
else:
    print("Better luck next time!")
"""