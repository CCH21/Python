with open("A.txt", "r") as fileA:
    strA = ''
    for letters in fileA:
        strA += letters
with open("B.txt", "r") as fileB:
    strB = ''
    for letters in fileB:
        strB += letters
strC = "".join(sorted(strA + strB))
with open("C.txt", "w") as fileC:
    fileC.write(strC)
