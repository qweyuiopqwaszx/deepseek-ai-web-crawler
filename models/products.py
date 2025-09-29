from pydantic import BaseModel


class products(BaseModel):
    """
    Represents the data structure of a Product.
    """

    name: str
    brand: str
    price: str
    type: str
    description: str