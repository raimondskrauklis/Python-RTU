user_temperature = input(f"Ievadiet savu ķermeņa temperatūru -> ")
user_temperature = float(user_temperature)
normal_temperature_lowest = 35
normal_temperature_highest = 37
if normal_temperature_lowest <= user_temperature <= normal_temperature_highest:
    print("Viss kārtībā")
else:
    print("Iespējams drudzis")
