import pytest
from csv_processor.args import parse_condition

def test_parse_condition_greater():
    column, op, value = parse_condition("rating>4.7")
    assert column == "rating"
    assert op == ">"
    assert value == "4.7"

def test_parse_condition_equal():
    column, op, value = parse_condition("price=avg")
    assert column == "price"
    assert op == "="
    assert value == "avg"

def test_parse_condition_less_equal():
    column, op, value = parse_condition("rating<=5")
    assert column == "rating"
    assert op == "<="
    assert value == "5"

def test_parse_condition_invalid():
    with pytest.raises(ValueError):
        parse_condition("rating!4.7")

def test_parse_condition_spaces():
    column, op, value = parse_condition("  rating   >   4.7  ")
    assert column == "rating"
    assert op == ">"
    assert value =="4.7"