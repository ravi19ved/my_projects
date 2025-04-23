import asyncio
 
async def fn():
    print('This is ')
    await asyncio.sleep(5)
    print('asynchronous programming')
    await asyncio.sleep(5)
    print('and not multi-threading')
 
asyncio.run(fn())