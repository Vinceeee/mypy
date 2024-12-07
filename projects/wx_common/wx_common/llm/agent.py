"""
定义一个智能体,调用工具
"""

import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_openai.chat_models import ChatOpenAI
from loguru import logger
from pydantic import SecretStr


@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b."""
    return a * b


def test_chat_with_tool():
    llm = ChatOpenAI(
        model="hunyuan-lite",
        base_url="https://api.hunyuan.cloud.tencent.com/v1",
        api_key=SecretStr(os.environ.get("API_KEY", "")),
    )
    tools = [multiply]
    agent = create_tool_calling_agent(
        llm,
        tools=tools,
        prompt=ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant"),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        ),
    )
    # return tool call message
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    logger.info(agent_executor.invoke(dict(input="what's the result of 10 times 4?")))


test_chat_with_tool()
