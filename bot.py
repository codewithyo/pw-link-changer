from telethon import TelegramClient, events
from telethon.tl.custom import Button
from os import getenv
from telethon.tl.types import ReplyKeyboardMarkup, KeyboardButtonRow, KeyboardButton

bot = TelegramClient(
    'Linkchanger',
    api_id = getenv("API_ID"),
    api_hash = getenv("API_HASH")

).start(
    bot_token = getenv("BOT_TOKEN")

)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("Hi, I am link changer of Physics Wallah")

        
@bot.on(events.NewMessage(pattern='https://'))
async def change(event):
    try:
        link_hash = event.raw_text.split('/')[3]
    except Exception as e:
        await conv.send_message(e)

    async with bot.conversation(event.chat_id, timeout=200) as conv:
        try:
            await conv.send_message(
            'Choose quality',   
            buttons = ReplyKeyboardMarkup(
                rows=[
                    KeyboardButtonRow(
                        buttons=[
                            KeyboardButton(text="240"),
                            KeyboardButton(text="360"),
                            KeyboardButton(text="480"),
                            KeyboardButton(text="720"),
                        ]
                    )
                ],
                resize=True,
                persistent=True,
                placeholder="Choose quality"
            ))

            msg2 = await conv.get_response()
            await msg2.respond(
                f"https://d26g5bnklkwsh4.cloudfront.net/{link_hash}/hls/{msg2.raw_text}/main.m3u8",
                buttons = Button.clear()
                
            )
        except TimeoutError:
            await event.respond(
                f"Timed out, try again",
                buttons = Button.clear()
                
            )


bot.run_until_disconnected()
