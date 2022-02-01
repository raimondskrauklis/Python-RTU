room_height = input(f"Ievadiet telpas augstumu (m): -> ")
room_height = int(room_height)
room_width = input(f"Ievadiet telpas dziļumu (m): -> ")
room_width = int(room_width)
room_length = input(f"Ievadiet telpas platumu (m): -> ")
room_length = int(room_length)
room_volume = room_height * room_width * room_length
print(f"Telpas tilpums ir {room_volume} kubikmetri.")