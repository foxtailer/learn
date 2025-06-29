from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class OrderLineSchema(BaseModel):
    orderid: str | None = 'order-001'
    sku: str
    qty: int = Field(gt=0)


class BatchSchema(BaseModel):
    reference: str | None = 'batch-001'
    sku: str
    eta: Optional[date]
    qty: int = Field(gt=0)
