import logging
from telethon import TelegramClient, events, sync

# Konfigurasi API
api_id = 'API ID'
api_hash = 'API HASH'

# Inisialisasi Telegram Client
client = TelegramClient('userbot_session', api_id, api_hash)

# Mengatur level logging
logging.basicConfig(level=logging.WARNING)

# Dictionary untuk menyimpan jumlah warn setiap pengguna
warn_count = {}

# Command untuk menangani pesan yang masuk
@client.on(events.NewMessage(pattern='/start'))
async def handle_start(event):
    await event.respond('Halo! Saya adalah Userbot Telegram.')
    raise events.StopPropagation

# Command untuk menangani pesan yang masuk
@client.on(events.NewMessage(pattern='/ping'))
async def handle_ping(event):
    await event.respond('Pong!')
    raise events.StopPropagation

# Command untuk menangani pesan pribadi
@client.on(events.NewMessage(private=True))
async def handle_private_message(event):
    sender_id = event.sender_id
    if sender_id in warn_count:
        warn_count[sender_id] += 1
        if warn_count[sender_id] > 5:
            await client.edit_permissions(event.chat_id, sender_id, view_messages=False)
            await event.reply('Anda telah diblokir karena melanggar aturan.')
        else:
            await event.reply(f'**Renn Asisten Scurity**\nMohon Jangan Spam, Tunggu Balasan Nya\n\n{warn_count[sender_id]}/5')
    else:
        warn_count[sender_id] = 1
        await event.reply(f'**Renn Asisten Scurity**\nMohon Jangan Spam, Tunggu Balasan Nya\n\n{warn_count[sender_id]}/5')

# Menjalankan Userbot
with client:
    client.run_until_disconnected()
