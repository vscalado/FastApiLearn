import asyncio

async def sum(a, b):
    return a + b

coro = sum(2,3)



#Event Loop
event_loop = asyncio.new_event_loop()
result =event_loop.run_until_complete(coro)
print(result)