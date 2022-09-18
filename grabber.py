from pyrogram import Client
from colorama import init, Fore
from pyrogram.enums import ChatType

init()
print(f"{Fore.CYAN}TGGrabber by @retr0dev")
# api_id = int(input("Введи API ID: "))
# api_hash = input("Введи API HASH: ")
api_id = 17759008
api_hash = "2614a46c633ccf2a91f390d13b1531c8"
app = Client("session", api_id=api_id, api_hash=api_hash)


async def main():
    async with app:
        me = await app.get_me()
        print(f"{Fore.GREEN}Вы вошли как {me.first_name}")
        print(f"{Fore.CYAN}Выберите канал для выгрузки:")
        async for dialog in app.get_dialogs():
            if getattr(dialog, "chat", None) and dialog.chat.type == ChatType.CHANNEL:
                print(f"[+]{Fore.BLUE}{dialog.chat.title} {Fore.GREEN}({dialog.chat.id})")
        grab_channel_id = int(input("Введите ID канала: "))
        post_channel_id = int(input("Введите ID канала для публикации: "))
        print(f"{Fore.CYAN}Начинаю выгрузку...")
        async for message in app.get_chat_history(grab_channel_id):
            if getattr(message, "service", None):
                continue
            await message.forward(post_channel_id)
        print(f"{Fore.GREEN}Выгрузка завершена!")
        input("Нажмите Enter для выхода...")


if __name__ == '__main__':
    app.run(main())
