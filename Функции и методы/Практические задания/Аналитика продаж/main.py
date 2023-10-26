def calculate_total_sales(sales_list):
    # TODO Вычислите общую стоимость проданных товаров из списка `sales_list`
    result: int = 0
    for item in sales_list:
        result += item["quantity"] * item["price_per_unit"]

    return result


sales_data = [
    {"product": "Футболка", "quantity": 10, "price_per_unit": 500},
    {"product": "Джинсы", "quantity": 5, "price_per_unit": 1000},
    {"product": "Кроссовки", "quantity": 3, "price_per_unit": 1500},
]

# TODO Вызовете функцию calculate_total_sales и передайте в функцию значение переменной sales_data
print(f"Общая стоимость проданных товаров: {calculate_total_sales(sales_data)}")
