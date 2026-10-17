from pydantic import BaseModel, Field


class OrderLine(BaseModel):
    sku: str
    quantity: int = Field(gt=0)
    unit_price: int  # in cents


class Order(BaseModel):
    id: str
    customer_id: str
    lines: list[OrderLine]

    def total(self) -> int:
        return sum(line.quantity * line.unit_price for line in self.lines)
