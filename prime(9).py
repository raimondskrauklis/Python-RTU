number = input(f"Ievadiet skaitli pārbaudei - > ")
number = int(number)
if number <= 1:
    print(number, "nav pirmskaitlis.")
else:
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            print(number, "nav pirmskaitlis.")
            break
    else:
        print(number, "ir pirmskaitlis.")
