from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str
    password: str  
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserIn(SQLModel):
    username: str
    password: str
    email: str