"""Asyncio adds concurrency to your program without adding new threads"""

import asyncio
import random

async def print_names():
    for name in ("John", "Kate", "Mike", "Alex", "Ann"):
        print(name)
        await asyncio.sleep(random.uniform(0.5, 1.5))

async def print_ages(min_sleep, max_sleep):
    for _ in range(5):
        print(random.randint(20, 50))
        await asyncio.sleep(random.uniform(min_sleep, max_sleep))

loop = asyncio.get_event_loop()

tasks = [print_names(), print_ages(0.2, 1)]

loop.run_until_complete(asyncio.gather(*tasks))

loop.close()