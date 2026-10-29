"""Учёт заказов: исправленный код после анализа Pylint (задание 1788)."""


class Order:
    """Заказ с идентификатором и суммой."""

    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total

    def get_total(self):
        """Возвращает сумму заказа."""
        return self.total

    def apply_discount(self, percent):
        """Применяет скидку в процентах и возвращает новую сумму."""
        self.total = self.total * (100 - percent) / 100
        return self.total


def print_order(order):
    """Печатает номер заказа и его сумму."""
    print("Заказ", order.order_id, "на сумму", order.get_total())


if __name__ == "__main__":
    first_order = Order(1, 500)
    print_order(first_order)
