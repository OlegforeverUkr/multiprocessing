import asyncio
import time


async def power_async(num):
    result = num ** 10_000_000
    return result


async def main():
    start_time = time.time()

    tasks = [power_async(i) for i in [2, 3, 5]]
    results = await asyncio.gather(*tasks)

    return time.time() - start_time


if __name__ == '__main__':
    print(asyncio.run(main()))
