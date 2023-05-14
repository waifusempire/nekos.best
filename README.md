# nekos.best

## A simple wrapper around the nekos.best api, supports sync and async envs

---

## Install

```txt
windows: pip install git+https://github.com/waifusempire/nekos.best  
linux/darwin: pip3 install git+https://github.com/waifusempire/nekos.best
```

## Example

```py
# synchronous Example
from nekosbest import Client

with Client() as client:
    smile_result = client.get("smile")[0]
    pout_results = client.get("pout", 3)

print(smile_result, pout_results)
```

---

```py
# asynchronous Example
from nekosbest import AsyncClient
import asyncio


async def main():
    async with AsyncClient() as client:
        smile_result = (await client.get("smile"))[0]
        pout_results = await client.get("pout", 3)

    print(smile_result, pout_results)

asyncio.run(main())
```
