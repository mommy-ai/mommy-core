"""MOMMY AI Configuration."""
import os
from dataclasses import dataclass

@dataclass
class Config:
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_base_url: str = os.getenv("LLM_BASE_URL", "https://api.deepseek.com/v1")
    llm_model: str = os.getenv("LLM_MODEL", "deepseek-chat")
    coingecko_url: str = "https://api.coingecko.com/api/v3"
    max_history: int = int(os.getenv("MAX_HISTORY", "20"))
    temperature: float = float(os.getenv("TEMPERATURE", "0.8"))

config = Config()
