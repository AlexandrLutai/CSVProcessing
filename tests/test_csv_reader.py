import os
import tempfile
import pytest
from csv_processor.csv_reader import read_csv

def test_read_csv_returns_list_of_dicts():
    csv_content = "name,price\nitem1,10\nitem2,20\n"
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv', encoding='utf-8') as tmp:
        tmp.write(csv_content)
        tmp_path = tmp.name

    try:
        result = read_csv(tmp_path)
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[0] == {'name': 'item1', 'price': '10'}
        assert result[1] == {'name': 'item2', 'price': '20'}
    finally:
        os.remove(tmp_path)

def test_read_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_csv('non_existent_file.csv')