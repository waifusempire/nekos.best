from .client import AsyncClient, Client
from .errors import NekosBestBaseError, NotFoundError, APIError
from .extra import NekosBestCategories
from .nekosbestconfig import __author__, __version__


__version__ = "0.1.0"
__all__ = ("AsyncClient", "Client", "NekosBestBaseError", "NotFoundError", "APIError", "NekosBestCategories")