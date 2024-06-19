import asyncio

import requests

async def get_response(url):
    response = requests.get(url)
    return response.content

async def get_response_status(url):
    response = requests.get(url)
    print(response.status_code)

async def sleepy_coro(delay, _id):
    await asyncio.sleep(delay)
    print(f"Coro {_id} done")

async def example():
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    return 100

async def main():
    example_result = await example()
    print("The first coro ", example_result)

async def tasks_main():
    task1 = asyncio.create_task(sleepy_coro(5, 1))
    task2 = asyncio.create_task(sleepy_coro(3, 2))

    await task1
    await task2

async def cherry_dumplings():
    result = await get_response("https://klopotenko.com/vareniki-z-vishneu/")
    print(result)

async def collect_data():
    urls = [
        "https://klopotenko.com/vareniki-z-vishneu/",
        "https://python.org"
    ]
    async with asyncio.TaskGroup() as group:
        for url in urls:
            group.create_task(get_response_status(url))

if __name__ == "__main__":
    # coro = main()
    # asyncio.run(coro)
    # asyncio.run(tasks_main())
    # asyncio.run(cherry_dumplings())
    asyncio.run(collect_data())
