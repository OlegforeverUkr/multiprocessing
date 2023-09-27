import asyncio
import time
import aiohttp

url_google = "https://google.com"
url_rozetka = "https://rozetka.com.ua/"
url_microsoft = "https://microsoft.com"


async def get_status(index, session):
    response = await session.get(url_google)
    result = response.text
    print(f'response from {index}')
    return result


async def response_site(urls):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        for _ in urls:
            result = await asyncio.gather(*[get_status(index, session) for index in range(5)])
    print('ok')
    return time.time() - start


if __name__ == "__main__":
    print(asyncio.run(response_site([url_google, url_rozetka, url_microsoft])))


