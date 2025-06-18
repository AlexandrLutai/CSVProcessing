from typing import List, Dict, Optional
from tabulate import tabulate

def print_table(data: List[Dict[str, str]], headers: Optional[str] = "keys") -> None:
    """
    Выводит данные в виде таблицы с помощью tabulate.
    Разделители столбцов — |, угловой символ — +.
    :param data: список словарей (строк)
    :param headers: заголовки таблицы (по умолчанию — ключи словаря)
    """
    if not data:
        print("Нет данных для отображения.")
        return
    print(tabulate(data, headers=headers, tablefmt="grid", stralign="center", numalign="center"))

