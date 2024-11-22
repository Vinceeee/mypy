"""
一个包含OTEL链路追踪的api服务

请求会打到otel collector

otel collector可以起一个jaeger的实例
"""

from fastapi import FastAPI
import redis.asyncio
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.sdk.resources import Resource


# 定义资源并设置 service.name
resource = Resource.create(attributes={"service.name": "my-fastapi-app"})

# 初始化 TracerProvider
trace.set_tracer_provider(TracerProvider(resource=resource))
# 配置 OTLP 导出器
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# 创建 FastAPI 应用
app = FastAPI()

# 初始化 Redis
rins = redis.asyncio.Redis(host="localhost", port=6379)

# 自动检测 FastAPI 应用
FastAPIInstrumentor.instrument_app(app)
RedisInstrumentor().instrument()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/{item_id}")
async def put_item(item_id: int, value: str):
    await rins.set(str(item_id), value)
    return {"item_id": item_id, "message": "OK"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "value": await rins.get(str(item_id))}
