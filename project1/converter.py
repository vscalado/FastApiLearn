import requests
from os import getenv
import aiohttp
from fastapi import HTTPException

ALPHAVANTAGE_APINEY = "74VX1WKU2N2WDH41"

def sync_converter(from_currency:str, to_currency:str, price:float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APINEY}'
    try:
        response = requests.get(url=url, verify=False)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f'Error: {error}')
    
    data = response.json()

    if 'Realtime Currency Exchange Rate' not in data:
        raise HTTPException(status_code=400, detail=f'Error: Realtime Currency Exchange Rate not in response {data}')

    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return price * exchange_rate

async def async_converter(from_currency:str, to_currency:str, price:float):

    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APINEY}'
    print(url)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url, verify_ssl=False) as response:
                data = await response.json()

    except Exception as error:
        raise HTTPException(status_code=400, detail=f'Error: {error}')

    if 'Realtime Currency Exchange Rate' not in data:
        raise HTTPException(status_code=400, detail=f'Error: Realtime Currency Exchange Rate not in response {data}')

    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return {to_currency: price * exchange_rate}


