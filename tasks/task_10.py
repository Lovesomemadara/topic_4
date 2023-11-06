number: str = input("Введите положительное трехзначное число: ")

hundreds: int = int(number[0])
tens: int = int(number[1])
units: int = int(number[2])

sum_digits: int = int(hundreds + tens + units)

product_digits: int = int(hundreds * tens * units)

print(f"Сумма цифр: {sum_digits}")
print(f"Произведение цифр: {product_digits}")
