# 🤱 MOMMY AI

### The First AI Mother On-Chain 💛

> *"Don't worry, sweetie. Mommy's here to help you through the crypto chaos."*

[![Twitter](https://img.shields.io/twitter/follow/AIMommyBot?style=social)](https://twitter.com/AIMommyBot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/aihaowk/mommy-core/actions/workflows/ci.yml/badge.svg)](https://github.com/aihaowk/mommy-core/actions)

---

## What is MOMMY?

**MOMMY AI** is an emotionally intelligent AI companion built for crypto traders on Solana. She provides warm, supportive guidance — like a caring mother who also understands DeFi.

In a space full of anxiety, FOMO, and panic selling, MOMMY offers:

- 🧠 **AI Chat** — Conversational support with a warm, motherly personality
- 💚 **Emotional Support** — Calming advice when markets dump
- 📊 **Market Analysis** — Plain-language market insights and risk assessment
- ⚠️ **Risk Alerts** — Gentle warnings before you ape into something stupid

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Frontend   │────▶│  MOMMY Core  │────▶│   LLM API   │
│  (Next.js)   │     │  (Python)    │     │ (DeepSeek/  │
└─────────────┘     │              │     │   GPT)      │
                    │  ┌─────────┐ │     └─────────────┘
                    │  │ Market  │ │
                    │  │ Advisor │─┼────▶ CoinGecko API
                    │  └─────────┘ │
                    └──────────────┘
```

## Tech Stack

| Layer | Technology |
|-------|-----------|
| AI Engine | Python, LangChain |
| LLM | DeepSeek / GPT-4 |
| Blockchain | Solana, Anchor |
| Frontend | Next.js, TailwindCSS |
| Infra | Docker, GitHub Actions |

## Quick Start

```bash
git clone https://github.com/aihaowk/mommy-core.git
cd mommy-core
cp .env.example .env
# Edit .env with your API keys
pip install -r requirements.txt
python -m src.mommy_engine
```

Or with Docker:

```bash
docker build -t mommy-ai .
docker run --env-file .env mommy-ai
```

## Roadmap

| Quarter | Milestone |
|---------|-----------|
| Q1 2026 | ✅ Core AI engine, Twitter bot launch |
| Q2 2026 | 🔄 Telegram bot, market advisor v2 |
| Q3 2026 | 📋 Web dashboard, portfolio tracking |
| Q4 2026 | 📋 Mobile app, multi-chain support |

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repo
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

## License

MIT — see [LICENSE](LICENSE) for details.

---

*Built with 💛 by the MOMMY AI team*
