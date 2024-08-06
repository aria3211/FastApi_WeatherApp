from fastapi import FastAPI
from pydantic import BaseModel



class Location(BaseModel):
    name:str
    region:str
    country:str
    tz_id:str
    localtime:str

class Current(BaseModel):
    last_updated_epoch:int
    last_updated:str
    temp_c:float
    temp_f:float
    is_day:int

class Condition(BaseModel):
    text:str
    icon:str
    code:int

class Weather(BaseModel):
    location : Location
    current: Current