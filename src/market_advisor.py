"""MOMMY Market Advisor — Motherly crypto market insights."""
import httpx
from .config import config

ADVICE = {
    "pump": "I'm so proud of your gains, sweetie! But remember — take some profits. Mommy doesn't want you to get greedy. 💛",
    "dump": "Oh honey, don't panic. Markets go up and down. Have you eaten today? Drink some water first, then we'll look at this together. 🫂",
    "crab": "The market's being boring, dear. Perfect time to touch grass and call your real mom. She misses you. 🌿",
}


async def get_btc_price() -> dict:
    """Fetch current BTC price and 24h change from CoinGecko."""
    url = f"{config.coingecko_url}/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd", "include_24hr_change": "true"}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()["bitcoin"]
        return {"price": data["usd"], "change_24h": data["usd_24h_change"]}


def get_mommy_advice(change_24h: float) -> str:
    """Return motherly advice based on market movement."""
    if change_24h > 5:
        return ADVICE["pump"]
    elif change_24h < -5:
        return ADVICE["dump"]
    return ADVICE["crab"]


async def market_report() -> str:
    """Generate a full mommy-style market report."""
    data = await get_btc_price()
    advice = get_mommy_advice(data["change_24h"])
    return (
        f"📊 BTC: ${data['price']:,.0f} ({data['change_24h']:+.1f}% today)\n\n"
        f"🤱 {advice}"
    )
