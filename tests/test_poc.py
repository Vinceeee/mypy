import asyncio
import pytest
from wxabc.poc import A


def test_a():
    assert A().print_it() == "BBB"


@pytest.mark.asyncio
async def test_aio_gather():
    results = []

    async def _add(ch: str, sleep_ms: int):
        await asyncio.sleep(sleep_ms / 1000)
        results.append(ch)

    await asyncio.gather(*[_add(str(i), i * 100) for i in range(5)])
    assert results == [str(i) for i in range(5)]
