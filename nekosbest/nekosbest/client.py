import aiohttp
import requests


from .nekosbestconfig import BASE_URL, AIOHTTP_HEADERS, REQUESTS_HEADERS
from .errors import NotFoundError, APIError
from .extra import Result, NekosBestCategories


class AsyncClient:
    def __init__(self, api_version: int = 2):
        self.__url = BASE_URL.format(version=api_version)
        self.__closed = True
        self.__session = None

    def create_session(self):
        self.__session = aiohttp.ClientSession(self.__url, headers=AIOHTTP_HEADERS)
        self.__closed = False

    async def close_session(self):
        await self.__session.close()
        self.__closed = True

    async def __aenter__(self):
        self.create_session()
        return self
    
    async def __aexit__(self):
        await self.close_session()

    @property
    def closed(self):
        return self.__closed

    async def __get(self, endpoint: str, amount: int) -> dict:
        if self.closed:
            raise aiohttp.ClientError("Client is closed")

        params = {"amount": amount} if amount > 1 else {}

        async with self.__session.get(f"/{endpoint}", params=params) as response:
            if response.status == 404:
                raise NotFoundError
            elif not response.ok:
                raise APIError(response.status)

            data = await response.json()
        
        return data
    
    async def get(self, category: str = None, amount: int = 1):
        category = category or NekosBestCategories.random()
        results = await self.__get(category, amount)
        return [Result(result) for result in results["results"]]

    async def endpoints(self):
        return await self.__get("endpoints", 0)
    


class Client:
    def __init__(self, api_version: int = 2):
        self.__url = BASE_URL.format(version=api_version)
        self.__closed = True
        self.__session = None

    def create_session(self):
        self.__session = requests.Session()
        self.__closed = False

    def close_session(self):
        self.__session.close()
        self.__closed = True

    def __enter__(self):
        self.close_session()
        return self
    
    def __exit__(self, *err):
        self.close_session()

    @property
    def closed(self):
        return self.__closed
    
    def __get(self, endpoint: str, amount: int) -> dict:
        if self.closed:
            raise requests.ConnectionError("Client is closed")
        
        params = {"amount": amount} if amount > 1 else {}

        with self.__session.get(f"{self.__url}/{endpoint}", params=params, headers=REQUESTS_HEADERS) as response:
            if response.status_code == 404:
                raise NotFoundError
            elif not response.ok:
                raise APIError(response.status_code)
            
            data = response.json()

        return data
     
    def get(self, category: str = None, amount: int = 1) -> list[Result]:
        category = category or NekosBestCategories.random()
        results = self.__get(category, amount)
        return [Result(result) for result in results["results"]]
    
    def endpoints(self):
        return self.__get("endpoints", 0)