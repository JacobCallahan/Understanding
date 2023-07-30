"""aiohttp is a great library for interacting with http requests"""

import asyncio
import aiohttp
import time

async def get_status(url):
    print(f"Getting status of {url}")
    start_time = time.monotonic()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            total_time = time.monotonic() - start_time
            print(f"Finished getting status of {url} in {total_time:.2f} seconds")
            return url, response.status

urls = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.github.com",
    "https://www.linkedin.com"
]

async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_status(url))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        try:
            url, code = await task
            print(f"Status code for {url} is {code}")
        except Exception as err:
            print(f"Task failed! {err}")

asyncio.run(main())
