"""
Программа для рассчета налога с продаж
Версия: 1.0
Автор: Инна
"""

#Исходные данные8
price = 69.8
amount = 4
tax = 0.20

#Выполнение рассчетов
total_price = round(price * amount,2)
tax_from_sale = round(total_price * tax,2)
price_without_tax = round(total_price - tax_from_sale,2)

print("Цена покупки", total_price)
print("Включая налог", tax_from_sale)