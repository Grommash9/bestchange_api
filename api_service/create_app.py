from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

app = FastAPI()

from api_service import db


def params_control(base_currency, target_currency,
                   min_order_size, max_order_size,
                   min_volume, max_volume, currency_list):
    if max_volume is not None and min_volume is not None:
        if max_volume < min_volume:
            raise ValueError('max_volume is smaller then min_volume are you sure?')
    if min_order_size is not None and max_order_size is not None:
        if max_order_size < min_order_size:
            raise ValueError('max_order_size is smaller then min_order_size are you sure?')

    if base_currency not in currency_list or target_currency not in currency_list:
        raise TypeError('There is no currency with that id, please check currencies '
                        'IDs on one of these endpoints /currency_codes or /currency_names')


def city_enter_control(city_id, city_list):
    if city_id not in city_list:
        raise KeyError(f'city id {city_id} not found, you can get cites ids on /city_list endpoint')


@app.get("/currency_names")
async def currency_names():
    return await db.currency_names.get_all()


@app.get("/city_list")
async def city_list():
    return await db.city.get_all()


@app.get("/currency_codes")
async def currency_codes():
    return await db.currency_codes.get_all()


@app.get("/exchange_names")
async def exchange_names():
    return await db.exchange.get_all()


@app.post("/exchange_data")
async def get_exchange_rates(base_currency: int, target_currency: int,
                             min_order_size: float = 0, max_order_size: float = 99999999,
                             min_volume: float = 0, max_volume: float = 99999999):
    currency_list = [currency['currency_id'] for currency in await db.currency_codes.get_all()]
    try:
        params_control(base_currency, target_currency, min_order_size, max_order_size, min_volume, max_volume,
                       currency_list)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'error': f"{e}"})
    return await db.rates.get_for_pair(base_currency, target_currency, min_volume, max_volume, min_order_size,
                                       max_order_size)


@app.post("/get_all_from_city")
async def get_exchange_rates(city_id: int):
    try:
        city_id_list = [city['city_id'] for city in await db.city.get_all()]
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'error': f"{e}"})
    city_enter_control(city_id, city_id_list)
    return await db.rates.get_all_from_city(city_id)


@app.post("/get_pair_in_city")
async def get_exchange_rates(base_currency: int, target_currency: int, city_id: int,
                             min_order_size: float = 0, max_order_size: float = 99999999,
                             min_volume: float = 0, max_volume: float = 99999999):
    try:
        currency_list = [currency['currency_id'] for currency in await db.currency_codes.get_all()]
        params_control(base_currency, target_currency, min_order_size, max_order_size, min_volume, max_volume,
                       currency_list)
        city_id_list = [city['city_id'] for city in await db.city.get_all()]
        city_enter_control(city_id, city_id_list)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'error': f"{e}"})
    return await db.rates.get_pair_in_city(base_currency, target_currency,
                                           min_volume, max_volume, min_order_size, max_order_size,
                                           city_id)


@app.post("/get_rate_pair_in_city")
async def get_exchange_rates(base_currency: int, target_currency: int, city_id: int,
                             min_order_size: float = 0, max_order_size: float = 99999999,
                             min_volume: float = 0, max_volume: float = 99999999):
    try:
        currency_list = [currency['currency_id'] for currency in await db.currency_codes.get_all()]
        params_control(base_currency, target_currency, min_order_size, max_order_size, min_volume, max_volume,
                       currency_list)
        city_id_list = [city['city_id'] for city in await db.city.get_all()]
        city_enter_control(city_id, city_id_list)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'error': f"{e}"})
    return await db.rates.get_rate_pair_in_city(base_currency, target_currency,
                                                min_volume, max_volume, min_order_size, max_order_size,
                                                city_id)


@app.post("/exchange_rate")
async def get_exchange_rates(base_currency: int, target_currency: int,
                             min_order_size: float = 0, max_order_size: float = 99999999,
                             min_volume: float = 0, max_volume: float = 99999999):
    currency_list = [currency['currency_id'] for currency in await db.currency_codes.get_all()]
    try:
        params_control(base_currency, target_currency, min_order_size, max_order_size, min_volume, max_volume,
                       currency_list)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'error': f"{e}"})
    return await db.rates.get_rate_for_pair(base_currency, target_currency, min_volume, max_volume, min_order_size,
                                            max_order_size)


@app.post("/get_all_rate_pair_in_city")
async def get_exchange_rates(base_currency: int, target_currency: int, city_id: int,
                             min_order_size: float = 0, max_order_size: float = 99999999,
                             min_volume: float = 0, max_volume: float = 99999999):
    try:
        currency_list = [currency['currency_id'] for currency in await db.currency_codes.get_all()]
        params_control(base_currency, target_currency, min_order_size, max_order_size, min_volume, max_volume,
                       currency_list)
        city_id_list = [city['city_id'] for city in await db.city.get_all()]
        city_enter_control(city_id, city_id_list)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'error': f"{e}"})
    return await db.rates.get_all_rate_pair_in_city(city_id)
