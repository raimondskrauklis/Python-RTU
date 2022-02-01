tree_height = input(f"Ievadiet egles augstumu -> ")
tree_height = int(tree_height)
z = tree_height - 1
x = 1
for i in range(tree_height):
    print(' ' * z + '+' * x + ' ' * z)
    x += 2
    z -= 1



