per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада  "))

tkb = per_cent.get('ТКБ')
ckb = per_cent.get('СКБ')
vtb = per_cent.get('ВТБ')
sber = per_cent.get('СБЕР')

deposit1 = tkb*money
deposit2 = ckb*money
deposit3 = vtb*money
deposit4 = sber*money

deposits = [deposit1, deposit2, deposit3,deposit4]
maxdeposit = max(deposits)
print("Максимальная сумма, которую вы можете заработать —", maxdeposit)
