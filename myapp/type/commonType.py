from datetime import datetime
from pydantic import BaseModel

class Titem(BaseModel):
    title : str
    description : str
    amount : int
    customer : int


