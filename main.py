from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api import api_get_weather
from models.model import Weather,Location,Current

app = FastAPI()



@app.get("/weather/{city}")
async def read_root(city:str=None):
    res = await  api_get_weather(city)
    weather = Weather(**res)
    html_content = f"""
    <html>
        <head>
            <title>Weather app</title>
        </head>
        <body>
            <h1>Weather for {weather.location.name} in {weather.location.country} is:</h1>
            <br>
            <p>{weather.current.temp_c}</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)




