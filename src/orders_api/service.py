from orders_api.models import Order


class OrderService:
    def __init__(self) -> None:
        self._orders: dict[str, Order] = {}

    def create(self, order: Order) -> Order:
        if order.id in self._orders:
            raise ValueError(f"order {order.id} already exists")
        self._orders[order.id] = order
        return order

    def get(self, order_id: str) -> Order | None:
        return self._orders.get(order_id)
