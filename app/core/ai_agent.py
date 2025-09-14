from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

#Our project is multi ai agent., for this we will be using the LangGraph.
from langgraph.prebuilt import create_react_agent
from langchain_core.message.ai import AIMessage

from app.config.settings import settings

#Note if you don't allow the allow_search then the tavily will not be used.
def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):


    llm = ChatGroq(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(

        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    #You are starting a conversation history. with the below text:
    state = {"messages": query}  #Previous conversation history., whatever the user has said till now.

    response = agent.invoke(state)

    messages = response.get("messages")

    # Fetching the message when it is only the AI Message.
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    #Now I want only the latest message from the AI. as below
    ai_messages[-1]

    







