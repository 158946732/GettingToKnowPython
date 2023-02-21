#Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))
sum = 0
if number > 99 and number < 1000:
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    print(f"Сумма цифр в числе равна: {sum}")    
else: print("Вы ввели неверное число!")
