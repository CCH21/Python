import string

file = open("practice_99.txt", "r")
article = ''
for line in file:
    article += line
file.close()
article = article.lower()
list1 = article.split()
list2 = []

for words in list1:
    word = ''
    for char in words:
        if char not in string.whitespace + string.punctuation:
            word += char
    list2.append(word)

d = {}
for key in list2:
    if key not in d:
        d[key] = 1
    if key in d:
        d[key] += 1
d = dict(sorted(d.items(), key=lambda x: x[1]))
for key, d[key] in d.items():
    if d[key] > 10:
        print('\nWord: ' + key)
        print('Number: ' + str(d[key]))
