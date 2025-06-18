
import csv

def read_csv(filepath: str) -> list[dict[str, str]]:
    """
    Читает CSV-файл и возвращает список словарей, где ключи — названия колонок.
    :param filepath: путь к CSV-файлу
    :return: список строк в виде словарей
    """
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)