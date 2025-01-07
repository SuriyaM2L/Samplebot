from pyrogram import Client, filters


API_ID = "7851526"
API_HASH = "93ba4db0ad662e558356871afe8ca6de"
BOT_TOKEN = "7737992517:AAHVqoKAEmn8dZzPfD-3hjOKMdNCT4wvLuk"

CodeRed = Client(
    name="SampleBot",
    api_id=API_ID,
    api-hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("bot has stated")

CodeRed.run()
