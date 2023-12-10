from pydantic import BaseModel, ConfigDict


class Order(BaseModel):
    username: str
    items: list[str]

    model_config = ConfigDict(from_attributes=True)


class OrderWithId(Order):
    id: int

