from csv_processor.output import print_table

def test_print_table_empty(capsys):
    print_table([])
    captured = capsys.readouterr()
    assert "Нет данных для отображения." in captured.out

def test_print_table_output(capsys):
    data = [
        {"name": "item1", "price": "10"},
        {"name": "item2", "price": "20"}
    ]
    print_table(data)
    captured = capsys.readouterr()
    assert "name" in captured.out
    assert "price" in captured.out
    assert "item1" in captured.out
    assert "item2" in captured.out
    assert "+" in captured.out

