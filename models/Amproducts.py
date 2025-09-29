from pydantic import BaseModel


class products(BaseModel):
    """
    Represents the data structure of a Product.
    """
    name: str
    merchantname: str
    discountedprice: str
    originalprice: str
    rating: str
    numberofreviews: str
    freeshipping: str
    description: str