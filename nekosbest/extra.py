import random
from typing import Optional


class NekosBestCategories:
    categories = [
        highfive := "highfive",
        happy := "happy",
        sleep := "sleep",
        handhold := "handhold",
        laugh := "laugh",
        bite := "bite",
        poke := "poke",
        tickle := "tickle",
        kiss := "kiss",
        wave := "wave",
        thumbsup := "thumbsup",
        stare := "stare",
        cuddle := "cuddle",
        smile := "smile",
        baka := "baka",
        blush := "blush",
        nom := "nom",
        think := "think",
        pout := "pout",
        facepalm := "facepalm",
        wink := "wink",
        shoot := "shoot",
        smug := "smug",
        nope := "nope",
        cry := "cry",
        pat := "pat",
        nod := "nod",
        punch := "punch",
        dance := "dance",
        feed := "feed",
        shrug := "shrug",
        bored := "bored",
        kick := "kick",
        hug := "hug",
        yeet := "yeet",
        slap := "slap",
        neko := "neko",
        husbando := "husbando",
        kitsune := "kitsune",
        waifu := "waifu"
    ]

    @classmethod
    def random(self):
        return random.choice(self.categories)


class Result:
    def __init__(self, data: dict):
        self.data = data

        self.url: Optional[str] = data.get("url")
        self.anime_name: Optional[str] = data.get("anime_name")
        self.source_url: Optional[str] = data.get("source_url")
        self.artist_name: Optional[str] = data.get("artist_name")
        self.artist_href: Optional[str] = data.get("artist_href")

    def __repr__(self):
        return f"Result< url: {self.url!r}, anime_name: {self.anime_name!r}, source_url: {self.source_url!r}, artist_name: {self.artist_name!r}, artist_href: {self.artist_href!r} >"