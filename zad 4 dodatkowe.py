dice = {}
kosc = []

for i in range (2,13):
    for j in range (1,min(i,7)):
        kosc.append((j, i - j))
    dice[i] = kosc.copy()

    kosc.clear()



print(dice)


print ("blablablablablablalasdflaslda")