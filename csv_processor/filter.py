
def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def filter_data(
    data: list[dict[str, str]],
    column: str,
    operator: str,
    value: str
) -> list[dict[str, str]]:
    """
    Фильтрует список словарей по значению в указанной колонке с заданным оператором.
    Поддерживаются операторы: '>', '<', '='.
    Для числовых значений сравнение происходит как чисел, для остальных — как строк.
    """
    if operator not in ('>', '<', '='):
        raise ValueError(f"Недопустимый оператор: {operator}")

    result = []
    for row in data:
        if column not in row:
            raise KeyError(f"Колонка '{column}' отсутствует в данных")
        a = row[column]
        b = value
        if is_number(a) and is_number(b):
            a_val = float(a)
            b_val = float(b)
        else:
            a_val = a
            b_val = b

        if operator == '>':
            if a_val > b_val:
                result.append(row)
        elif operator == '<':
            if a_val < b_val:
                result.append(row)
        else:  # '='
            if a_val == b_val:
                result.append(row)
    return result