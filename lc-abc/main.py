import asyncio
from loguru import logger

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.callbacks.file import FileCallbackHandler
from langchain.agents import AgentExecutor, create_tool_calling_agent

from lc_abc.tools.functions import do_sum

api_key = "sk-Vm6FF5vmBwqEBruwAsEWijFDt15pMtn4nrIBcDmO5ILwX6p2"


def main():
    loop = asyncio.get_event_loop()
    task = loop.create_task(agent_call())
    for _ in range(100):
        loop.run_until_complete(asyncio.sleep(1))
        if task.done():
            logger.info("task completed.")
            break
    else:
        logger.info("task not completed.")


async def agent_call():
    llm = ChatOpenAI(
        base_url="https://api.moonshot.cn/v1/",
        api_key=api_key,
        model="moonshot-v1-8k",
        streaming=True,
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant"),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    callback = FileCallbackHandler("./callback.log")
    tools = [do_sum]
    agent = create_tool_calling_agent(llm, tools=tools, prompt=prompt)

    numbers = list(range(10))
    ae = AgentExecutor(agent=agent, tools=[do_sum], callbacks=[callback], verbose=True)
    results = []

    async for each in ae.astream_events(
        {"input": f"what is the sum of {numbers}, please use tools."}, version="v2"
    ):
        results.append(each)
        logger.info(each)


# asyncio.run(agent_call())
main()
