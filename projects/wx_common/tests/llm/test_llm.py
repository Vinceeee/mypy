import os

import pytest
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings


@pytest.mark.skipif(
    not all([os.environ.get("OPENAI_API_KEY"), os.environ.get("OPENAI_API_BASE")]), reason="API_KEY not set"
)
class TestLangchainOpenai:
    chat_model_name = "Qwen/Qwen3-8B"

    def test_chat(self):
        chat_model = ChatOpenAI(model=self.chat_model_name, streaming=True)
        for each in chat_model.stream("just tell me what's the result of 1+1/no_think"):
            print(each)

    @pytest.mark.skipif(
        not all([os.environ.get("OPENAI_API_KEY"), os.environ.get("OPENAI_API_BASE")]), reason="API_KEY not set"
    )
    def test_embedding(self):
        model = "BAAI/bge-m3"
        embeddings = OpenAIEmbeddings(model=model)
        print(embeddings.embed_query("hello world"))

    def test_openai(self):
        from openai import OpenAI

        # 创建OpenAI客户端
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), base_url=os.environ.get("OPENAI_API_BASE"))

        # 创建聊天补全请求
        response = client.chat.completions.create(
            model=self.chat_model_name, messages=[{"role": "user", "content": "1+1等于多少？\no think"}], stream=True
        )

        # 处理流式响应
        for chunk in response:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
