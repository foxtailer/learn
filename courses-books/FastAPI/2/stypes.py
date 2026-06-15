from pydantic import BaseModel, Field


class BookM(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., gt=1900, lt=2100)


class AllBookM(BaseModel):
    title: str
    author: str


class UserM(BaseModel):
    name: str
    email: str

    model_config = {
        "from_attributes": True
    }
'''
@field_validator("age")
def validate_age(cls, value):
if value < 18 or value > 100:
raise ValueError(
"Age must be between 18 and 100"
)
return value
'''

class AllUserM(BaseModel):
    name: str

    model_config = {
        "from_attributes": True
    }

