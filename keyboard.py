from aiogram import types

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(types.KeyboardButton('Панель администратора'))

adm = types.ReplyKeyboardMarkup(resize_keyboard=True)
adm.add(types.KeyboardButton('Чёрный Список'),
        types.KeyboardButton('Добавить в ЧС'),
        types.KeyboardButton('Убрать из ЧС'))
adm.add(types.KeyboardButton('Рассылка'))
adm.add('Назад')

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(types.KeyboardButton('Отмена'))

usr = types.ReplyKeyboardMarkup(resize_keyboard=True)
usr.add(types.KeyboardButton('Расписание'), types.KeyboardButton('Рейтинг'),
        types.KeyboardButton('Часто задаваемые вопросы')
        # types.KeyboardButton('')
        )


def fun(user_id):
  quest = types.InlineKeyboardMarkup(row_width=3)
  quest.add(
    types.InlineKeyboardButton(text='Ответить',
                               callback_data=f'{user_id}-ans'),
    types.InlineKeyboardButton(text='Удалить', callback_data='ignor'))
  return quest
