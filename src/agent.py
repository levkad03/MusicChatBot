from langchain.agents import Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq

from src.config import GROQ_API_KEY
from src.tools.genius import GeniusLyricsTool
from src.tools.wikipedia import get_wikipedia_tool

llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant", temperature=0)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="Wikipedia",
        func=get_wikipedia_tool().run,
        description="General music history",
    ),
    Tool(
        name="LyricsFinder",
        func=GeniusLyricsTool().run,
        description="Find lyrics of songs",
    ),
    Tool(
        name="WebSearch",
        func=search.run,
        description="Useful for finding up-to-date or specific music info from the web, including lyrics, artist history, or song meanings",
    ),
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True,
)
