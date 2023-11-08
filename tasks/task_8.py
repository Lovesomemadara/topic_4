interval: int = int(input(
    "Введите величину временного интервала в минутах: "
))

hours: int = interval // 60
minutes: float = interval % 60

print(f"Результат: {hours} часа {minutes} минут")
