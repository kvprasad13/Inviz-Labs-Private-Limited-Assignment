from pydantic import BaseModel
from typing import Optional
class Property(BaseModel):
    property_name:str
    address:str
    city:str
    state:str 

