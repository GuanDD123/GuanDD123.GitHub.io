import aiohttp
from yarl import URL
from _typeshed import FileDescriptorOrPath


async def send_request():
    async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout) as session:
        async with session.get(url=URL(val=str, encoded=True),
                               params=dict) as resp:
            pass


async def response_info_content(resp: aiohttp.ClientResponse):
    resp.url
    resp.status
    resp.headers

    await resp.text()
    await resp.read()
    await resp.json()


async def streaming():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=str) as resp:

            await resp.content.read(n=int['chunk_size'])

            with open(FileDescriptorOrPath, 'wb') as f:
                async for chunk in resp.content.iter_chunked(n=int['chunk_size']):
                    f.write(chunk)
