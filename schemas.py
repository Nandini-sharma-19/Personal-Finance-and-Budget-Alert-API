from pydantic import BaseModel,Field
class UserCreate(BaseModel):
    username: str = Field(...,min_length=3,max_length=50,description="Username must be between 3 and 50 characters")
    monthly_limit:float=Field(default=10000.0,gt=0,description="Monthly budget limit must be greater than zero")

class UserResponse(BaseModel):
    id:int
    username:str
    monthly_limit:float
    class Config:
        from_attributes=True