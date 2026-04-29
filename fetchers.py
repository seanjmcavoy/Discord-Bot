import httpx

async def get_cat(session: httpx.AsyncClient)-> str:
    url = "https://api.thecatapi.com/v1/images/search"
    resp = await session.get(url)
    resp.raise_for_status()
    return resp.json()[0]['url']

async def get_dog(session: httpx.AsyncClient) -> str:
    url = "https://random.dog/woof.json"
    resp = await session.get(url)
    resp.raise_for_status()
    return resp.json()['url']


