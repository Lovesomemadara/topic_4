number: str = input("Введите четырехзначное число: ")

thousands: int = int(number[0])
hundreds: int = int(number[1])
tens: int = int(number[2])
units: int = int(number[3])

print(f"Цифра в позиции тысяч: {thousands}")
print(f"Цифра в позиции сотен: {hundreds}")
print(f"Цифра в позиции десятков: {tens}")
print(f"Цифра в позиции единиц: {units}")
