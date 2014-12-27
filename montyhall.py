import random

#Returns 1 if the original selection wins
def PlayGame():
    i = [0,0,1]
    random.shuffle(i)
    #print "Game is: ",i
    
    selected = random.randrange(0,3)
    #print "Player Selects: ",selected

    while(True):
        remove = random.randrange(0,3)
        if (i[remove] == 0):
            break

    #print "Monty removes: ",remove
    
    return i[selected] == 1

selectedWin = 0
switchedWin = 0
i=0
for i in range(0,10000):
    if (PlayGame() == True):
        print "Sticker Wins!"
        selectedWin +=1
    else:
        print "Switcher Wins!"
        switchedWin +=1
        
print "Switcher wins ",switchedWin
print "Sticker wins ",selectedWin

