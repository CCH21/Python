fp = open("practice_83.txt", "w")
ch = input()
while ch != '#':
    fp.write(ch)
    print(ch)
    ch = input()
fp.close()
