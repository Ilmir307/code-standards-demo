"""Расчёт цены со скидкой: исправленный код (задание 1788)."""


def calculate_discount(price, percent):
    """Возвращает цену товара со скидкой в процентах."""
    result = price * (100 - percent) / 100
    return result


if __name__ == "__main__":
    final_price = calculate_discount(1000, 10)
    print("Цена со скидкой:", final_price)
