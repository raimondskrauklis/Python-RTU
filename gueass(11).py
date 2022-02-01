sentence = input(f"Ievadiet vārdu vai teikumu -> ")
word = ""
for i in sentence:
    if i != " ":
        word += "*"
    else:
        word += " "
print(f"Teikums, kurš jāuzmin: {word}")
player = input("Ievadiet burtu ->  ")
for i in sentence:
    if player == i:
        print(i, end="")
    elif i == " ":
        print(i, end="")
    else:
        print("*", end="")
