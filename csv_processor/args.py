import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Обработка CSV-файла с фильтрацией и агрегацией"
    )
    parser.add_argument(
        "--file", "-f",
        required=True,
        help="Путь к CSV-файлу"
    )

    subparsers = parser.add_subparsers(dest="command")

    
    where_parser = subparsers.add_parser("where", help="Фильтрация по условию")
    where_parser.add_argument(
        "condition",
        help='Условие фильтрации, например: "rating>4.7"'
    )

    
    aggregate_parser = subparsers.add_parser("aggregate", help="Агрегация по колонке")
    aggregate_parser.add_argument(
        "condition",
        help='Условие агрегации, например: "rating=avg"'
    )
    
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

