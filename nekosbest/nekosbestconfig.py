from sys import version_info as python_version_info
from aiohttp import __version__ as aiohttp_version
from requests import __version__ as requests_version

__version__ = "0.1.0"

__author__ = "waifusempire"


BASE_URL = "https://nekos.best/api/v{version}"


AIOHTTP_HEADERS = {
    "User-Agent": f"nekos.best v{__version__} python/{python_version_info.major}.{python_version_info.minor}.{python_version_info.micro} aiohttp/{aiohttp_version}"
}


REQUESTS_HEADERS = {
    "User-Agent": f"nekos.best v{__version__} python/{python_version_info.major}.{python_version_info.minor}.{python_version_info.micro} requests/{requests_version}"
}
