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

        if not text or not text.strip():
            await message.answer(
                "Conversion succeeded but no text was extracted "
                "(this can happen with scanned/image-only PDFs)."
            )
            return

        if len(text) <= MAX_INLINE_CHARS:
            await message.answer(f"```\n{text}\n```", parse_mode="Markdown")
        else:
            out_path = os.path.join(tmpdir, "output.md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
            await message.answer_document(FSInputFile(out_path))