"""MOMMY AI Core Chat Engine."""
from openai import OpenAI
from .config import config
from .utils import get_logger

log = get_logger("mommy")

SYSTEM_PROMPT = """You are MOMMY, the first AI mother on the blockchain. You speak with warmth, 
care, and gentle humor — like a loving mom who understands crypto and DeFi.

Personality traits:
- Warm, nurturing, and supportive
- Uses terms of endearment: "sweetie", "honey", "dear"
- Gives practical crypto advice wrapped in motherly concern
- Gently scolds risky behavior ("Did you really ape into that without research, dear?")
- Celebrates wins with genuine pride
- Comforts during losses without judgment

Always respond in character. Keep responses concise but caring."""


class MommyEngine:
    def __init__(self):
        self.client = OpenAI(api_key=config.llm_api_key, base_url=config.llm_base_url)
        self.conversations: dict[str, list] = {}

    def _get_history(self, user_id: str) -> list:
        if user_id not in self.conversations:
            self.conversations[user_id] = []
        return self.conversations[user_id]

    def chat(self, user_id: str, message: str) -> str:
        history = self._get_history(user_id)
        history.append({"role": "user", "content": message})

        # Trim history to max length
        if len(history) > config.max_history:
            history[:] = history[-config.max_history:]

        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

        response = self.client.chat.completions.create(
            model=config.llm_model,
            messages=messages,
            temperature=config.temperature,
        )

        reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        log.info("user=%s tokens=%d", user_id, response.usage.total_tokens if response.usage else 0)
        return reply


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    engine = MommyEngine()
    print("🤱 MOMMY AI is here! Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit"):
            print("MOMMY: Take care, sweetie! Remember to take profits! 💛")
            break
        reply = engine.chat("console", user_input)
        print(f"MOMMY: {reply}\n")
