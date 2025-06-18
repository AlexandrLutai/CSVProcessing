import pytest
from csv_processor.aggregate import aggregate_column

@pytest.fixture
def sample_data():
    return [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'},
        {'name': 'poco x5 pro', 'brand': 'xiaomi', 'price': '299', 'rating': '4.4'},
    ]

def test_aggregate_avg(sample_data):
    result = aggregate_column(sample_data, 'price', 'avg')
    assert result == pytest.approx((999 + 1199 + 199 + 299) / 4)

def test_aggregate_min(sample_data):
    result = aggregate_column(sample_data, 'price', 'min')
    assert result == 199

def test_aggregate_max(sample_data):
    result = aggregate_column(sample_data, 'price', 'max')
    assert result == 1199

def test_aggregate_rating_avg(sample_data):
    result = aggregate_column(sample_data, 'rating', 'avg')
    assert result == pytest.approx((4.9 + 4.8 + 4.6 + 4.4) / 4)

def test_aggregate_invalid_column(sample_data):
    with pytest.raises(KeyError):
        aggregate_column(sample_data, 'not_exist', 'avg')

def test_aggregate_invalid_operation(sample_data):
    with pytest.raises(ValueError):
        aggregate_column(sample_data, 'price', 'sum')

def test_aggregate_non_numeric(sample_data):
    with pytest.raises(ValueError):
        aggregate_column(sample_data, 'brand', 'avg')

def test_aggregate_empty_data():
    with pytest.raises(ValueError):
        aggregate_column([], 'price', 'avg')