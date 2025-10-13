TAX = 0.2
price = float(input("Введіть ціну товару: "))
vat = price * TAX
total = price + vat
print("Сума ПДВ:", vat)
print("Загальна вартість з ПДВ:", total)
