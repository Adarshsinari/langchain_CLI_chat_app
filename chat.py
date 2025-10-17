import os
from secret import OAI_KEY, SERP_API_KEY
os.environ["OPENAI_API_KEY"] = OAI_KEY
os.environ["SERPAPI_API_KEY"] = SERP_API_KEY
from langchain_openai import OpenAI
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory

lang_model = OpenAI(temperature = 0)

chat_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

search = SerpAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for seraching the Internet and getting info about test player"
    )
]

agent_chain = initialize_agent(
    tools=tools, 
    llm=lang_model,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=chat_memory
    )

print(agent_chain.invoke({"input":"Who is the current best test player?"}))

while True:
    print("Hey, it's LangC! type 'quit' to exit.")
    i = input("Ask me: ")
    if i =="quit":
        print("Thanks!!")
        break
    else:
        print(agent_chain.invoke({"input": i}))