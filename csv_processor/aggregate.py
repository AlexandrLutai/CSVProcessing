from typing import List, Dict, Literal, Optional

def aggregate_column(
    data: List[Dict[str, str]],
    column: str,
    operation: Literal['avg', 'min', 'max']
) -> Optional[float]:
    """
    Выполняет агрегацию по числовой колонке: среднее (avg), минимум (min), максимум (max).
    :param data: список строк (словарей)
    :param column: имя числовой колонки
    :param operation: тип агрегации ('avg', 'min', 'max')
    :return: результат агрегации или None, если данных нет
    """
    if not data:
        raise ValueError("Нет данных для агрегации")
    if column not in data[0]:
        raise KeyError(f"Колонка '{column}' отсутствует в данных")
    if operation not in ('avg', 'min', 'max'):
        raise ValueError(f"Недопустимая операция агрегации: {operation}")

    try:
        values = [float(row[column]) for row in data]
    except ValueError as e:
        raise ValueError(f"Значения в колонке '{column}' не являются числами: {e}")

    if not values:
        return None

    if operation == 'avg':
        return sum(values) / len(values)
    elif operation == 'min':
        return min(values)
    elif operation == 'max':
        return max(values)