first_number: float = float(input("Введите первое число: "))
second_number: float = float(input("Введите второе число: "))

result: float = first_number > second_number

print(f"Число {first_number} больше числа {second_number} "
      f"это - {result}")
