with open("test.txt", "a") as file:
    string = input()
    string = string.upper()
    file.write(string)
