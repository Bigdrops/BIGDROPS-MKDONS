# BIGDROPS-MKDONS



![Python](https://img.shields.io/badge/python-3.12-blue)




![Status](https://img.shields.io/badge/status-paused-yellow)




![Telegram](https://img.shields.io/badge/platform-Telegram-26A5E4)



A Telegram bot wrapper around [Microsoft's MarkItDown](https://github.com/microsoft/markitdown).

Send it a file, it converts it to Markdown and replies.

**Bot:** [@Bigdropsmd_bot](https://t.me/Bigdropsmd_bot)
**Status:** Working locally, paused for now.

---

## Why this exists

Saw a TikTok about Microsoft's MarkItDown tool and wanted to see how far I could push it —
forked it, wired it into a Telegram bot to test file-to-markdown conversion on the fly from
my phone. Mostly a "let's see if this actually works" build.

## What it does

- Send a document (PDF, Word, Excel, PowerPoint) and the bot replies with the Markdown version
- `/start` for a quick intro

## What it doesn't do yet

- Photos sent via Telegram's photo picker aren't handled (only documents)
- No OCR — MarkItDown reads image metadata, not image text, without a vision model attached
- No YouTube transcription support (left out for now)
- Not deployed — only runs while manually started on a local machine

## Stack

- Python 3.12
- aiogram 3.15.0
- markitdown (pdf, docx, pptx, xlsx, audio, azure doc-intel/content-understanding extras)
- python-dotenv

## Running it

\`\`\`powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python bot.py
\`\`\`

Needs a `.env` file with:
\`\`\`
BOT_TOKEN=your_telegram_bot_token
\`\`\`

## If I pick this back up

- Add photo support
- Wire in OCR (OpenAI vision or Azure Document Intelligence)
- Deploy somewhere that doesn't depend on my PC staying on

---

Built for fun, to mess around with an idea I saw online. Use at your own risk.
