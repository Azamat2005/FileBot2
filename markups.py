from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


DeleteBtn = KeyboardButton('Delete file')
MyFile = KeyboardButton("All my file")
SendMyFiles = KeyboardButton("Send My file")
markups = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
markups.add(DeleteBtn, MyFile, SendMyFiles)
