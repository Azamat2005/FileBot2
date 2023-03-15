import logging
from markups import markups
from downloader import Download, DeleteFolder
import FileNames
import os
from aiogram import Bot, Dispatcher, executor,types

API_TOKEN = '5775603853:AAGrBSp6w5oYjpo56qa3TDEaWLa5GxFu1vo'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_function(message: types.Message):

    await bot.send_message(chat_id=message.chat.id, text="Salom Bot ga xush kelibsiz", reply_markup=markups)

@dp.message_handler(content_types=['text'])
async def getUrl(message: types.Message):
    UserId = message.chat.id


    if message.text.startswith('https://') or len(message.text) > 20:
        await bot.send_message(chat_id=message.chat.id, text="Hozir")

        if not os.path.isdir(f'./Download/{UserId}'):
            os.mkdir(f'./Download/{UserId}')
        else:
            print("Mavjud")
            pass


        url = message.text
        output_path = f'./Download/{UserId}/'
        try:
            Download(url, output_path)
        except:
            pass
        await bot.send_message(chat_id=message.chat.id, text="Yuklandi",)

    if message.text == "Send My file":

        print("True")

        try:
            userId = message.chat.id

            pathId = f"./Download/{userId}/"
            fileList = FileNames.FileFInder(pathId)
        except:
            pass


        try:
            for fileName in fileList:
                file_path = f"./Download/{UserId}/{fileName}"
                await bot.send_document(chat_id=message.chat.id, document=types.InputFile(file_path))

        except:
            await bot.send_message(message.chat.id, text="Xato")

    if message.text == "Delete file":
        try:
            paths = f"./Download/{UserId}/"
            DeleteFolder(paths)
        except:
            pass
        try:
            await bot.send_message(chat_id=message.chat.id, text="Deleted all file successfully")
        except:
            await bot.send_message(chat_id=message.chat.id, text="Your folder already clear")

    if message.text == "All my file":

        try:
            if len(FileNames.FileFInder(f'./Download/{UserId}/')) >= 1 :

                for fileN in FileNames.FileFInder(f'./Download/{UserId}/'):
                    await bot.send_message(chat_id=message.chat.id, text=fileN)
            else:
                await bot.send_message(chat_id=message.chat.id, text="Your folder is empty")
        except:
            pass
async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)