from typing import Union, Annotated
from sqlalchemy import Column, String, Integer, Identity, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from enum import Enum
from pydantic import BaseModel, Field, HttpUrl

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Identity(start=10), primary_key=True)
    name = Column(String, index=True, nullable=False)
    hashed_password = Column(String)


class Person(BaseModel):
    url: HttpUrl
    name: Union[str, None] = None


class User_new(BaseModel):
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)] = None
    name: Union[str, None] = None
    person: Union[Person, None] = None


class Main_User(BaseModel):
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)] = None
    name: Union[str, None] = None


class Main_UserDB(Main_User):
    hashed_password: Annotated[Union[str, None], Field(max_length=200, min_length=6)] = None


class Good(BaseModel):
    id: Annotated[Union[int, None], Field(default=100, ge=1, lt=200)] = None
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = 0
    nalog: Union[float, None] = 13.6


class Tags(Enum):
    users = "users"
    advents = "advents"
    info = "info"
    good = "good"


class New_Response(BaseModel):
    message: str
