word1 = [a for a in input()]
word2 = [b for b in input()]
letters = set(word1)
wildCount = word2.count('*')
letterCount1 = [word1.count(i) for i in letters]
letterCount2 = [word2.count(i) for i in letters]
missing = 0
failed = False
for i in range(len(letterCount1)):
    if letterCount1[i] >= letterCount2[i]:
        missing += letterCount1[i] - letterCount2[i]
    else:
        failed = True
        break
if not failed:
    if 0<=missing<=wildCount:
        print('A')
    else:
        print('N')
else:
    print('N')
