import logging
import FileNames
import os
import dotenv
from markups import markups
from downloader import Download, DeleteFolder
from aiogram import Bot, Dispatcher, executor,types

dt = dotenv.dotenv_values('.env')


API_TOKEN = dt['TOKEN']
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_function(message: types.Message):

    await bot.send_message(chat_id=message.chat.id, text="Salom Bot ga xush kelibsiz", reply_markup=markups)

@dp.message_handler(content_types=['text'])
async def getUrl(message: types.Message):
    userid = message.chat.id


    if message.text.startswith('https://') or len(message.text) > 20:
        await bot.send_message(chat_id=message.chat.id, text="Hozir")

        if not os.path.isdir(f'./Download/{userid}'):
            os.mkdir(f'./Download/{userid}/')
        else:
            print("Mavjud")



        url = message.text
        output_path = f'./Download/{userid}/'

        Download(url, output_path)

        await bot.send_message(chat_id=message.chat.id, text="Yuklandi",)

    if message.text == "Send My file":

        try:
            userId = message.chat.id

            pathId = f"./Download/{userId}/"
            fileList = FileNames.FileFInder(pathId)

            for fileName in fileList:
                file_path = f"./Download/{userid}/{fileName}"

                await bot.send_document(chat_id=userid, document=types.InputFile(file_path))
        except:

            await bot.send_message(message.chat.id, text="Xato")

    if message.text == "Delete file":
        try:
            paths = f"./Download/{userid}/"
            DeleteFolder(paths)
        except:
            pass

        try:
            await bot.send_message(chat_id=userid, text="Deleted all file successfully")
        except:
            await bot.send_message(chat_id=userid, text="Your folder already clear")

    if message.text == "Data":

        pathFile = f'./Download/{message.chat.id}/'

        fileList3 = FileNames.FileFInder(pathFile)

        for i in fileList3:
            try:
                pathFile += i
                await bot.send_document(message.chat.id, document=types.InputFile(pathFile))
            except:
                await bot.send_message(message.chat.id, text="Error")
    if message.text == "All my file":

        try:
            if len(FileNames.FileFInder(f'./Download/{userid}/')) >= 1 :

                for fileN in FileNames.FileFInder(f'./Download/{userid}/'):
                    await bot.send_message(chat_id=message.chat.id, text=fileN)
            else:
                await bot.send_message(chat_id=message.chat.id, text="Your folder is empty")
        except:
            await bot.send_message(chat_id=message.chat.id, text="Your folder is empty")
async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)