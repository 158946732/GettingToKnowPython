#Найдите сумму цифр трехзначного числа.
#*Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))
if (number < 100 or number > 999):
    print("Вы ввели неверное число!")
sum = 0
while number > 0:
    sum = sum + number % 10
    number = number // 10
print(f"Сумма цифр в числе равна: {sum}")