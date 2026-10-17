import pytest

from orders_api.models import Order, OrderLine
from orders_api.service import OrderService


def make_order(order_id: str = "o1") -> Order:
    return Order(id=order_id, customer_id="c1", lines=[OrderLine(sku="A", quantity=2, unit_price=150)])


def test_total():
    assert make_order().total() == 300


def test_duplicate_rejected():
    svc = OrderService()
    svc.create(make_order())
    with pytest.raises(ValueError):
        svc.create(make_order())
