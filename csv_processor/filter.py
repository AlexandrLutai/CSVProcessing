from typing import List, Dict

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False

def filter_data(
    data: List[Dict[str, str]],
    column: str,
    operator: str,
    value: str
) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению в указанной колонке с заданным оператором.
    Поддерживаются операторы: '>', '<', '='.
    Для числовых значений сравнение происходит как чисел, для остальных — как строк.
    Обрабатывает ошибки: отсутствующая колонка, неверный оператор, пустые данные.
    """
    if not data:
        raise ValueError("Данные для фильтрации пусты")
    if operator not in ('>', '<', '='):
        raise ValueError(f"Недопустимый оператор: {operator}")
    if column not in data[0]:
        raise KeyError(f"Колонка '{column}' отсутствует в данных")

    result = []
    for row in data:
        if column not in row:
            raise KeyError(f"Колонка '{column}' отсутствует в строке: {row}")
        a = row[column]
        b = value
        if is_number(a) and is_number(b):
            a_val = float(a)
            b_val = float(b)
        else:
            a_val = a
            b_val = b

        try:
            if operator == '>':
                if a_val > b_val:
                    result.append(row)
            elif operator == '<':
                if a_val < b_val:
                    result.append(row)
            else:  
                if a_val == b_val:
                    result.append(row)
        except Exception as e:
            raise ValueError(f"Ошибка при сравнении значений: {a_val} и {b_val}: {e}")
    return result