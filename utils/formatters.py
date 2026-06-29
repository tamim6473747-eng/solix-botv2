from typing import List, Dict, Any


def format_number(value):
    try:
        if value is None:
            return "0"
        if value >= 1_000_000:
            return f"{value/1_000_000:.2f}M"
        if value >= 1_000:
            return f"{value/1_000:.2f}K"
        return str(round(value, 2))
    except Exception:
        return "0"


def format_trending_message(tokens: List[Dict[str, Any]]) -> str:
    text = "🔥 <b>Top Trending Solana Tokens</b>\n\n"

    for i, token in enumerate(tokens, start=1):
        base = token.get("baseToken", {})
        name = base.get("name", "Unknown")
        symbol = base.get("symbol", "???")

        price = token.get("priceUsd", "0")
        liquidity = token.get("liquidity", {}).get("usd", 0)
        volume = token.get("volume", {}).get("h24", 0)
        url = token.get("url", "")

        text += (
            f"<b>{i}. {name} ({symbol})</b>\n"
            f"💰 Price: ${price}\n"
            f"💧 Liquidity: ${format_number(liquidity)}\n"
            f"📊 Volume (24h): ${format_number(volume)}\n"
            f"🔗 <a href='{url}'>View Chart</a>\n\n"
        )

    return text


def format_search_results(tokens: List[Dict[str, Any]]) -> str:
    text = "🔎 <b>Search Results</b>\n\n"

    if not tokens:
        return "❌ No tokens found."

    for token in tokens[:10]:
        base = token.get("baseToken", {})
        name = base.get("name", "Unknown")
        symbol = base.get("symbol", "???")
        address = base.get("address", "")
        price = token.get("priceUsd", "0")

        text += (
            f"<b>{name} ({symbol})</b>\n"
            f"💰 Price: ${price}\n"
            f"🧾 <code>{address}</code>\n\n"
        )

    return text


def format_token_details(token: Dict[str, Any]) -> str:
    if not token:
        return "❌ Token not found."

    base = token.get("baseToken", {})

    name = base.get("name", "Unknown")
    symbol = base.get("symbol", "???")
    address = base.get("address", "")

    price = token.get("priceUsd", "0")
    liquidity = token.get("liquidity", {}).get("usd", 0)
    volume = token.get("volume", {}).get("h24", 0)

    return (
        f"🪙 <b>{name} ({symbol})</b>\n\n"
        f"💰 Price: ${price}\n"
        f"💧 Liquidity: ${format_number(liquidity)}\n"
        f"📊 Volume (24h): ${format_number(volume)}\n\n"
        f"🧾 Contract:\n<code>{address}</code>"
      )
