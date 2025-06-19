from typing import Literal,Optional

def order_by(
    data: list[dict[str, str]],
    column: Optional[str],
    direction: Literal["asc", "desc"] = "asc"
) -> list[dict[str, str]]:
    """
    Сортирует список словарей по указанной колонке.
    :param data: список строк (словарей)
    :param column: имя колонки для сортировки
    :param direction: направление сортировки ('asc' или 'desc')
    :return: отсортированный список данных
    """
    if not column or not direction:
        return data  # сортировка не требуется

    reverse = direction == "desc"
    try:
        # Попробуем сортировать как числа, если возможно
        return sorted(
            data,
            key=lambda row: float(row[column]) if row[column].replace('.', '', 1).isdigit() else row[column],
            reverse=reverse
        )
    except Exception:
        # Если не получилось — сортируем как строки
        return sorted(data, key=lambda row: row[column], reverse=reverse)