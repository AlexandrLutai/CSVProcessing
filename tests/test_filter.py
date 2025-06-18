import pytest
from csv_processor.filter import filter_data

@pytest.fixture
def sample_data():
    return [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
        {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'},
    ]

def test_filter_price_greater(sample_data):
    result = filter_data(sample_data, 'price', '>', '300')
    assert len(result) == 2
    assert {row['name'] for row in result} == {'iphone 15 pro', 'galaxy s23 ultra'}

def test_filter_price_less(sample_data):
    result = filter_data(sample_data, 'price', '<', '300')
    assert len(result) == 2
    assert {row['name'] for row in result} == {'redmi note 12', 'poco x5 pro'}

def test_filter_brand_equal(sample_data):
    result = filter_data(sample_data, 'brand', '=', 'xiaomi')
    assert len(result) == 2
    assert all(row['brand'] == 'xiaomi' for row in result)

def test_filter_rating_equal(sample_data):
    result = filter_data(sample_data, 'rating', '=', '4.8')
    assert len(result) == 1
    assert result[0]['name'] == 'galaxy s23 ultra'

def test_invalid_operator(sample_data):
    with pytest.raises(ValueError):
        filter_data(sample_data, 'price', '!=', '999')