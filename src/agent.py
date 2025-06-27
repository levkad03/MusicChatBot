from langchain.agents import Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq

from config import GROQ_API_KEY
from tools.genius import GeniusLyricsTool
from tools.wikipedia import get_wikipedia_tool

llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant", temperature=0)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

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
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True,
)
