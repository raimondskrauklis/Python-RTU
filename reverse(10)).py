while True:
    name = input("Ievadiet savu vārdu -> ")
    reverse_name = name[::-1]
    print(f"{reverse_name.capitalize()}, pamatigs juceklis vai ne {name[0].upper()}?")
