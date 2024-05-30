from fastapi import APIRouter, Path, Query
from asyncio import gather
from converter import sync_converter, async_converter


router = APIRouter(prefix='/converter')

#Path Parameter
#Query Parameter
#Body Parameter
@router.get('/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
    to_currencies = to_currencies.split(',')

    result = []

    for currency in to_currencies:
        response = sync_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        result.append(response)

    return result

@router.get('/async/{from_currency}')
async def async_converter_router(
    from_currency: str = Path(max_length=3, regex='^[A-Z]{3}$'), 
    to_currencies: str = Query(max_length=50, regex='^[A-Z]{3}(,[A-Z]{3})*$'), 
    price: float = Query(gt=0)
    ):
    to_currencies = to_currencies.split(',')

    couroutines = []

    for currency in to_currencies:
        coro = async_converter(
            from_currency=from_currency,
            to_currency=currency,
            price=price
        )
        couroutines.append(coro)

    result = await gather(*couroutines)

    return result