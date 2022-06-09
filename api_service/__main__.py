from fastapi import FastAPI, Query
import uvicorn
from api_service import db

app = FastAPI()


@app.get("/city_list")
async def city_list():
    return await db.city.get_all()


@app.get("/currency_codes")
async def currency_codes():
    return await db.currency_codes.get_all()


@app.get("/currency_names")
async def currency_names():
    return await db.currency_names.get_all()


@app.get("/exchange_names")
async def exchange_names():
    return await db.exchange.get_all()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)