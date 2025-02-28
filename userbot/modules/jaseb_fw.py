from userbot import bot, CMD_HELP
from userbot.events import register
import asyncio

@register(outgoing=True, pattern=r"^\.fw(?:\s|$)(.*)")
async def jaseb_fw(event):
    args = event.pattern_match.group(1)
    if not args:
        await event.edit("❌ **Format Salah!** Gunakan `.fw <tujuan> <jeda> <jumlah>`")
        return
    
    try:
        tujuan, jeda, jumlah = args.split()
        jeda = float(jeda)
        jumlah = int(jumlah)
    except ValueError:
        await event.edit("❌ **Format Salah!** Gunakan `.fw <tujuan> <jeda> <jumlah>`")
        return

    await event.edit(f"✅ **Memulai Forward ke {tujuan}**\n🕒 Jeda: {jeda}s\n🔢 Jumlah: {jumlah}")

    for _ in range(jumlah):
        await bot.send_message(tujuan, "Pesan dari Jaseb FW 🚀")
        await asyncio.sleep(jeda)

CMD_HELP.update({
    "jaseb_fw": "**Jaseb FW**\n\n"
                "📌 **Perintah:** `.fw <tujuan> <jeda> <jumlah>`\n"
                "🔹 **Tujuan:** ID/Username grup atau user\n"
                "🔹 **Jeda:** Waktu delay antar pesan (dalam detik)\n"
                "🔹 **Jumlah:** Berapa kali pesan dikirim\n"
})
