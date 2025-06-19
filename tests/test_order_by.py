from csv_processor.order_by import order_by

def test_order_by_asc():
    data = [
        {"name": "b", "price": "20"},
        {"name": "a", "price": "10"},
        {"name": "c", "price": "30"},
    ]
    sorted_data = order_by(data, "name", "asc")
    assert [row["name"] for row in sorted_data] == ["a", "b", "c"]

def test_order_by_desc():
    data = [
        {"name": "b", "price": "20"},
        {"name": "a", "price": "10"},
        {"name": "c", "price": "30"},
    ]
    sorted_data = order_by(data, "price", "desc")
    assert [row["price"] for row in sorted_data] == ["30", "20", "10"]

def test_order_by_numeric_and_string():
    data = [
        {"name": "b", "price": "20"},
        {"name": "a", "price": "abc"},
        {"name": "c", "price": "10"},
    ]
    sorted_data = order_by(data, "price", "asc")
    
    assert [row["price"] for row in sorted_data] == ["10", "20", "abc"]

def test_order_by_no_column():
    data = [
        {"name": "b", "price": "20"},
        {"name": "a", "price": "10"},
    ]
    sorted_data = order_by(data, None, None)
    assert sorted_data == data  