import asyncio
import json
import random

import aiohttp
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

async def get_waifu(session: httpx.AsyncClient) -> str:
    url = "https://nekos.best/api/v2/neko"
    resp = await session.get(url)
    resp.raise_for_status()
    return resp.json()['results'][0]['url']

async def get_art(session: httpx.AsyncClient):
    with open("jsons/art.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    n = random.choice(data["objectIDs"])
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{n}"
    resp = await session.get(url)
    resp.raise_for_status()

    session.headers = None

    return resp.json()['primaryImage']

if __name__ == "__main__":
    session = httpx.AsyncClient()
    resp = asyncio.run(get_art(session))
    print(resp)

