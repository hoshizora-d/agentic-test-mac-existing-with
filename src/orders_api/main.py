from fastapi import FastAPI, HTTPException

from orders_api.models import Order
from orders_api.service import OrderService

app = FastAPI(title="orders-api")
service = OrderService()


@app.post("/orders", status_code=201)
def create_order(order: Order) -> Order:
    try:
        return service.create(order)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


@app.get("/orders/{order_id}")
def get_order(order_id: str) -> Order:
    order = service.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="not found")
    return order
