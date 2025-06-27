import requests
from langchain.tools import BaseTool

from src.config import GENIUS_API_KEY


class GeniusLyricsTool(BaseTool):
    name: str = "GeniusLyrics"
    description: str = "Use this to find the lyrics of a song by title and artist."

    def _run(self, query: str) -> str:
        headers = {"Authorization": f"Bearer {GENIUS_API_KEY}"}
        search_url = f"https://api.genius.com/search?q={query}"
        res = requests.get(search_url, headers=headers).json()
        hits = res["response"]["hits"]

        if not hits:
            return "No lyrics found"

        query_lower = query.lower()

        # Try to match song title AND artist name
        for hit in hits:
            song = hit["result"]
            title = song["title"].lower()
            artist = song["primary_artist"]["name"].lower()

            if all(keyword in f"{title} {artist}" for keyword in query_lower.split()):
                return f"Lyrics page: {song['url']}"

        # Fallback to first result if no good match found
        fallback = hits[0]["result"]
        return (
            f"Closest match: {fallback['full_title']}\nLyrics page: {fallback['url']}"
        )

    def _arun(self, query: str):
        raise NotImplementedError("Async not supported")
