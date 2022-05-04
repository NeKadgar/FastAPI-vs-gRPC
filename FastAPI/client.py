import asyncio
import aiohttp
import random
import string


LETTERS = string.ascii_letters


def get_users():
    with open("users.txt", "r") as file:
        return [user.split(":") for user in file.read().split("\n")]


def get_random_string():
    return ''.join(random.choice(LETTERS) for i in range(10))


async def async_hello(name, session):
    async with session.get(f'http://127.0.0.1:8000/hello/{name}') as response:
        res = await response.json()
        return res


async def async_add_user(session, first_name, last_name, age):
    async with session.post(f'http://127.0.0.1:8000/add_user', json={
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }) as response:
        res = await response.json()
        return res


async def async_auth_user(session, first_name, last_name, age):
    async with session.get(f'http://127.0.0.1:8000/auth_user', json={
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }) as response:
        res = await response.json()
        return res


async def async_main():
    # names = [get_random_string() for i in range(10000)]
    users = [user for user in get_users()]
    async with aiohttp.ClientSession() as session:
        # coros = [async_hello(name, session) for name in names]
        # coros = [async_add_user(session, *user) for user in users]
        coros = [async_auth_user(session, *user) for user in users]

        for coro in asyncio.as_completed(coros):
            response = await coro


if __name__ == "__main__":
    asyncio.run(async_main())
