num_switches: int = int(input("Введите количество переключателей: "))

combinations: int = 2 ** num_switches

print(f"Количество возможных комбинаций: {combinations}")
