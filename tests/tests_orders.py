import pytest
from src.orders import calculate_total

def test_calculate_total():
    order = {
        "items": [
            {"name": "item1", "price": 10.0, "quantity": 2},
            {"name": "item2", "price": 5.0, "quantity": 3}
        ],
        "member": True,
        "country": "PK"
    }
    assert calculate_total(order) == pytest.approx(35.0)