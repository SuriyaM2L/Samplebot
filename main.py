import pandas as pd
from datetime import datetime, timedelta
from pyrogram import Client, filters

# Load Excel Data
shutdown_data = pd.read_excel("TNPDCL - Planned Power Shutdown List.xlsx")

# Telegram Bot API Configuration
API_ID = "7851526"
API_HASH = "93ba4db0ad662e558356871afe8ca6de"
BOT_TOKEN = "7737992517:AAHVqoKAEmn8dZzPfD-3hjOKMdNCT4wvLuk"

app = Client("electricity_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Dictionary to store user data
user_data = {}

# Start Command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Welcome! Please send your location (area name) to get power shutdown updates.")

# Handle Location Input
@app.on_message(filters.text)
async def handle_location(client, message):
    area = message.text.strip().lower()
    user_id = message.from_user.id

    # Save user's area
    user_data[user_id] = area
    await message.reply(f"Got it! I will notify you about power shutdowns in {area}.")

# Scheduler to Notify Users
async def notify_users():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)

    # Filter shutdowns for tomorrow
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")
    shutdowns = shutdown_data[shutdown_data["Date"] == tomorrow_str]

    for user_id, area in user_data.items():
        matching_shutdowns = shutdowns[shutdowns["Area"].str.contains(area, case=False)]
        if not matching_shutdowns.empty:
            message = "Power Shutdown Alert for Tomorrow:\n"
            for _, row in matching_shutdowns.iterrows():
                message += f"- {row['Area']} from {row['Start Time']} to {row['End Time']}\n"
            await app.send_message(user_id, message)

# Schedule Notifications (Runs Every Hour)
@app.on_message(filters.command("schedule"))
async def schedule(client, message):
    while True:
        await notify_users()
        await asyncio.sleep(3600)  # Check every hour

app.run()
