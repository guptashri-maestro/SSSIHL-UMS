import datetime as dt
from pydantic import BaseModel, EmailStr, ConfigDict

class CreateEmployee(BaseModel):
    employee: int