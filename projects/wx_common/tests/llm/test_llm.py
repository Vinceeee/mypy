"""
使用Hunyuan API
[产品介绍](https://cloud.tencent.com/document/product/1729/104753)
"""

import os
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from pydantic import SecretStr


def test_chat():
    chat_model = ChatOpenAI(
        model="hunyuan-lite",
        base_url="https://api.hunyuan.cloud.tencent.com/v1",
        api_key=SecretStr(os.environ.get("API_KEY", "")),
    )
    result = chat_model.invoke("你是谁?")
    assert result


def test_embedding():
    embeddings = OpenAIEmbeddings(
        model="hunyuan-embedding",
        dimensions=1024,
        base_url="https://api.hunyuan.cloud.tencent.com/v1",
        api_key=SecretStr(os.environ.get("API_KEY", "")),
        check_embedding_ctx_length=False,
    )
    result = embeddings.embed_query("test")
    assert result
