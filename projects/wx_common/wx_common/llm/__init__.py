import os

from openai import OpenAI

# 构造 client
client = OpenAI(
    api_key=os.environ.get("HUNYUAN_API_KEY"),  # 混元 APIKey
    base_url="https://api.hunyuan.cloud.tencent.com/v1",  # 混元 endpoint
)


# 自定义参数传参示例
completion = client.chat.completions.create(
    model="hunyuan-pro",
    messages=[
        {
            "role": "user",
            "content": "你好",
        },
    ],
    extra_body={
        "enable_enhancement": True,  # <- 自定义参数
    },
)
