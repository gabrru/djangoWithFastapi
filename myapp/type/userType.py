from pydantic import BaseModel
    
class IUser(BaseModel):
    name: str
    age: int
    
    

