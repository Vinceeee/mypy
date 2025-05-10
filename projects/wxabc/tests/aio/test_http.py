import pytest
import aiohttp
import aioresponses


@pytest.mark.asyncio
async def test_aiohttp_web():
    with aioresponses.aioresponses() as _r:
        _r.get(
            "https://api.example.xyz/v1/check",
            payload={"code": 200, "message": "OK", "data": "pong"},
        )
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.example.xyz/v1/check") as resp:
                result = await resp.json()
                assert result["data"] == "pong"
