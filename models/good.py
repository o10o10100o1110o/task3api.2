from typing import Union, Annotated
from pydantic import BaseModel, Field, HttpUrl
class Main_User (BaseModel):
    name: Union[str, None] = None
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)] = None

class Main_UserDB(Main_User):
    password: Annotated[Union[str, None], Field(max_length=200, min_length=5)] = None

class New_Respons(BaseModel):
    message: str
