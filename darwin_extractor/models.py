from pydantic.fields import Field
from pydantic import BaseModel


class DarwinPurchaseResponse(BaseModel):
    product_name: str = Field(None, alias="productName")
    dc: str = Field(None)
    os: str = Field(None)
    cs: str = Field(None)
    mc: str = Field(None)
    rplus: str = Field(None)
    ra: str = Field(None)
    ex: str = Field(None)
    pf: str = Field(None)
    score: str = Field(None)
    rminus: str = Field(None)
    rs: str = Field(None)
    sc: str = Field(None)
    la: str = Field(None)
    cp: str = Field(None)
