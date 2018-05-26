from datetime import datetime
import asyncio

async def slow_routine():
    await asyncio.sleep(3)
    print("Time {}".format(datetime.now())) 


print(datetime.now())

list_func = []
for _ in range(3):
    list_func.append(slow_routine()) 

loop = asyncio.get_event_loop()


loop.run_until_complete(asyncio.gather(*list_func))

print(datetime.now())