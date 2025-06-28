from typing import Optional
from datetime import date

from pydantic import BaseModel, Field


class OrderLineSchema(BaseModel):
    orderid: str
    sku: str
    qty: int = Field(..., gt=0)


class BatchSchema(BaseModel):
    reference: str
    sku: str
    eta: Optional[date]
    qty: int
