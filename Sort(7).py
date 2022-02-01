choice_a = input(f"Ievadiet pirmo skaitli kārtošanai -> ")
choice_b = input(f"Ievadiet otro skaitli kārtošanai -> ")
choice_c = input(f"Ievadiet trešo skaitli kārtošanai -> ")
if choice_b < choice_a < choice_c:
    print(choice_b, choice_a, choice_c)
elif choice_a < choice_b < choice_c:
    print(choice_a, choice_b, choice_c)
elif choice_a < choice_c < choice_b:
    print(choice_a, choice_c, choice_b)
elif choice_c < choice_b < choice_a:
    print(choice_c, choice_b, choice_a)
elif choice_c < choice_a < choice_b:
    print(choice_c, choice_a, choice_b)
else:
    print(choice_b, choice_c, choice_a)
