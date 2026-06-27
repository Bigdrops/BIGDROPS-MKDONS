import asyncio
import logging
import os
import tempfile

from dotenv import load_dotenv
load_dotenv()

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from markitdown import MarkItDown

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
md = MarkItDown(enable_plugins=False)

MAX_INLINE_CHARS = 3500  # Telegram message limit is ~4096


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Send me a file (PDF, Word, Excel, PPT, image) and I'll convert it to Markdown."
    )


@dp.message(F.document)
async def handle_document(message: Message):
    doc = message.document
    await message.answer(f"Got it: {doc.file_name}. Converting…")

    with tempfile.TemporaryDirectory() as tmpdir:
        local_path = os.path.join(tmpdir, doc.file_name)
        file = await bot.get_file(doc.file_id)
        await bot.download_file(file.file_path, destination=local_path)

        try:
            result = md.convert(local_path)
            text = result.text_content
        except Exception as e:
            await message.answer(f"Conversion failed: {e}")
            return

        if len(text) <= MAX_INLINE_CHARS:
            await message.answer(f"```\n{text}\n```", parse_mode="Markdown")
        else:
            out_path = os.path.join(tmpdir, "output.md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
            await message.answer_document(FSInputFile(out_path))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())