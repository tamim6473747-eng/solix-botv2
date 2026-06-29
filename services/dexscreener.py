import aiohttp
from typing import List, Dict, Any

from config import (
    DEX_API_BASE,
    REQUEST_TIMEOUT,
    DEFAULT_HEADERS,
)


async def fetch_json(url: str) -> Dict[str, Any]:
    timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)

    async with aiohttp.ClientSession(
        timeout=timeout,
        headers=DEFAULT_HEADERS,
    ) as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise RuntimeError(
                    f"API request failed with status {response.status}"
                )
            return await response.json()


async def get_trending_tokens() -> List[Dict[str, Any]]:
    """
    Fetch trending tokens (DexScreener boosted/latest pairs)
    """
    url = f"{DEX_API_BASE}/search?q=solana"

    data = await fetch_json(url)

    pairs = data.get("pairs", [])

    # Sort by liquidity + volume (basic trending logic)
    sorted_pairs = sorted(
        pairs,
        key=lambda x: (
            x.get("liquidity", {}).get("usd", 0)
            + x.get("volume", {}).get("h24", 0)
        ),
        reverse=True,
    )

    return sorted_pairs[:10]


async def search_tokens(query: str) -> List[Dict[str, Any]]:
    url = f"{DEX_API_BASE}/search?q={query}"
    data = await fetch_json(url)
    return data.get("pairs", [])


async def get_token_by_address(address: str) -> Dict[str, Any]:
    url = f"{DEX_API_BASE}/tokens/{address}"
    data = await fetch_json(url)

    pairs = data.get("pairs", [])
    if not pairs:
        return {}

    return pairs[0]
