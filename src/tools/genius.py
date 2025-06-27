import requests
from langchain.tools import BaseTool

from config import GENIUS_API_KEY


class GeniusLyricsTool(BaseTool):
    name = "GeniusLyrics"
    description = "Use this to fetch songs lyrics from Genius"

    def _run(self, query: str) -> str:
        headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
        search_url = f"https://api.genius.com/search?q={query}"
        res = requests.get(search_url, headers=headers).json()
        hits = res["response"]["hits"]

        if not hits:
            return "No lyrics found"

        song_url = hits[0]["result"]["url"]

        return f"Lyrics page: {song_url}"

    def _arun(self, query: str):
        raise NotImplementedError("Async not supported")
