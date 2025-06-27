from src.agent import agent

if __name__ == "__main__":
    print("🎵 Welcome to MusicBot! Ask me anything about music.")
    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            break
        print("Bot:", agent.run(query))
