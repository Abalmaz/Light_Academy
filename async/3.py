import asyncio
from random import randint
from datetime import datetime


print(datetime.now())

async def some_request(n):
	numbers = [randint(0, 10) for _ in range(n)]
	for num in numbers:
		await squard_num(num)
		print(num)
	return numbers

async def squard_num(num):
	print(num ** 0.5) 

loop = asyncio.get_event_loop()
task = loop.run_until_complete(some_request(20))

print(datetime.now())

