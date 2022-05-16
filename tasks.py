print('Сколько билетов желаете приобрести?' '  ')
ticket = int(input())
price1 = 990
price2 = 1390
summa1 = 990 * ticket
summa2 = 1390 * ticket
print('Сколько Вам лет?' '  ')
age = int(input())
if age < 18:
    print('Для вас вход на конференцию бесплатный')
elif (18 <= age <= 25) and (ticket > 3):
    print('Стоимость билетов  ', (summa1 - (summa1 / 100 * 10)), 'рублей')
elif (18 <= age <= 25) and (ticket < 3):
    print('Стоимость билетов  ', summa1, 'рублей')
elif (age > 25) and (ticket > 3):
    print('Стоимость билетов  ', (summa2 - (summa2 / 100 * 10)), 'рублей')
else:
    print('Стоимость билетов  ', summa2, 'рублей')
