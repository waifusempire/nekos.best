class NekosBestBaseError(Exception):
    ...


class NotFoundError(NekosBestBaseError):
    ...


class APIError(NekosBestBaseError):
    def  __init__(self, errcode: int):
        self.error_code = errcode
