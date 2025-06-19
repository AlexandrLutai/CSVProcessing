import argparse

def add_order_by_argument(parser):
    parser.add_argument(
        "--order-by",
        help='Сортировка по колонке, например: "price=desc" или "brand=asc"'
    )

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Обработка CSV-файла с фильтрацией и агрегацией"
    )
    parser.add_argument(
        "--file", "-f",
        required=True,
        help="Путь к CSV-файлу"
    )
    add_order_by_argument(parser)

    subparsers = parser.add_subparsers(dest="command")

    where_parser = subparsers.add_parser("where", help="Фильтрация по условию")
    where_parser.add_argument(
        "condition",
        help='Условие фильтрации, например: "rating>4.7" или "brand=apple"'
    )
    add_order_by_argument(where_parser)

    aggregate_parser = subparsers.add_parser("aggregate", help="Агрегация по колонке")
    aggregate_parser.add_argument(
        "condition",
        help='Условие агрегации, например: "rating=avg"'
    )
    add_order_by_argument(aggregate_parser)

    return parser.parse_args()

def parse_condition(condition: str) -> tuple[str, str, str]:
    """
    Разбирает строку условия вида "rating>4.7" или "rating=avg" на (column, operator, value)
    """
    for op in ('>=', '<=', '>', '<', '='):
        if op in condition:
            column, value = condition.split(op, 1)
            return column.strip(), op, value.strip()
    raise ValueError("Некорректное условие. Используйте формат: column>value или column=operation")

def parse_order_by(order_by: str) -> tuple[str, str]:
    """
    Разбирает строку сортировки вида "price=desc" или "brand=asc" на (column, direction).
    :param order_by: строка сортировки
    :return: (column, direction)
    """
    if not order_by:
        return None, None
    if "=" in order_by:
        column, direction = order_by.split("=", 1)
        direction = direction.strip().lower()
        if direction not in ("asc", "desc"):
            raise ValueError("Сортировка поддерживает только 'asc' или 'desc'")
        return column.strip(), direction
    raise ValueError("Некорректный формат сортировки. Используйте: column=asc или column=desc")

