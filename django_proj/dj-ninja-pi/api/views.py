from ninja import Router
from django.core.cache import cache

router = Router()


@router.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@router.get("/incr")
async def incr(request, key: str):
    """通过表达式计算出结果"""
    value = cache.get(key)
    if not value:
        value = 0
    value += 1
    cache.set(key, value)
    return {"result": value}
