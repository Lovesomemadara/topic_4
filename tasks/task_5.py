wins: int = int(input("Введите количество побед: "))
draws: int = int(input("Введите количество ничейных игр: "))
losses: int = int(input("Введите количество поражений: "))

total_points: int = wins * 3 + draws

print(f"Общее количество очков: {total_points}")
