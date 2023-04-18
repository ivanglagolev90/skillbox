from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import pandas as pd
import xlrd
# from states import FSMContext, StateGroupExample





qss = {
    '1': ["EDW CK02 0000", "EDW CK02 2000", "EDZ CK02 0000", "EDZ CK02 2000"],
    '2': ["EDW CK04 0000", "EDW CK04 2000", "EDZ CK04 0000", "EDZ CK04 2000"],
    '3': ["EDW FK04 0000", "EDW FK04 2000", "EDZ FK04 0000", "EDZ FK04 2000"],
    '4': ["EDW FK06 0000", "EDW FK06 2000", "EDZ FK06 0000", "EDZ FK06 2000"],
    '5': ["EDW MK04 0000", "EDW MK04 2000", "EDZ MK04 0000", "EDZ MK04 2000"],
    '6': ["EDW MK06 0000", "EDW MK06 2000", "EDZ MK06 0000", "EDZ MK06 2000"],
    '7': ["EDW MK08 0000", "EDW MK08 2000", "EDZ MK08 0000", "EDZ MK08 2000"],
    '8': ["EDW MK10 0000", "EDW MK10 2000", "EDZ MK10 0000", "EDZ MK10 2000"],
    '9': ["EDW PK06 0000", "EDW PK06 2000", "EDZ PK06 0000", "EDZ PK06 2000"],
    '10': ["EDW PK08 0000", "EDW PK08 2000", "EDZ PK08 0000", "EDZ PK08 2000"],
    '11': ["EDW PK10 0000", "EDW PK10 2000", "EDZ PK10 0000", "EDZ PK10 2000"],
    '12': ["EDW SK06 0000", "EDW SK06 2000", "EDZ SK06 0000", "EDZ SK06 2000"],
    '13': ["EDW SK08 0000", "EDW SK08 2000", "EDZ SK08 0000", "EDZ SK08 2000"],
    '14': ["EDW SK10 0000", "EDW SK10 2000", "EDZ SK10 0000", "EDZ SK10 2000"],
    '15': ["EDS CK02 0000", "EDS CK02 2000"],
    '16': ["EDS CK04 0000", "EDS CK04 2000"],
    '17': ["EDS FK04 0000", "EDS FK04 2000"],
    '18': ["EDS FK06 0000", "EDS FK06 2000"],
    '19': ["EDS MK04 0000", "EDS MK04 2000"],
    '20': ["EDS MK06 0000", "EDS MK06 2000"],
    '21': ["EDS MK08 0000", "EDS MK08 2000"],
    '22': ["EDS MK10 0000", "EDS MK10 2000"],
    '23': ["EDS PK06 0000", "EDS PK06 2000"],
    '24': ["EDS PK08 0000", "EDS PK08 2000"],
    '25': ["EDS PK10 0000", "EDS PK10 2000"],
    '26': ["EDS SK06 0000", "EDS SK06 2000"],
    '27': ["EDS SK08 0000", "EDS SK08 2000"],
    '28': ["EDS SK10 0000", "EDS SK10 2000"]
}
API_TOKEN = '6208496245:AAEvLBNQCQBdjXVLaPGQR8Lv4lFc9KXOeGs'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
pices = []


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="ХОЧУ"),
            types.KeyboardButton(text="ПОИСК")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Зачем Вам бот? "
                        "Быстро узнать о наличии продукции и оформить заказ."
                        " Что умеет бот ? Показывать наличие и принимать заказ, отправлять коммерческое"
                        " предложение. "
                        "Как работает бот? Просто нажми ХОЧУ,"
                        " после приветствия Бота. далее Герман,"
                        " написать нужный Вам артикул \n"
                        "GZL MK06 1061B \n"
                        "или \n"
                        "DKL CK02 1085S\n"
                        "после чего Герман сориентирует Вас по наличию количества \n"
                        "на складе или предложит альтернативу", reply_markup=keyboard)
    # await message.reply()


@dp.message_handler()
async def echo(message: types.Message):
    msg = message.text
    print(msg)
    alt = ''
    #res = ''
    df = pd.read_excel("C:\\task\\ostatki.xls")
    #print(df)
    df_abc = df[df["Артикул"] == msg]
    #print(df_abc)
    for row in df_abc.iterrows():
        qeq = str(row)
        qeq = qeq.split("\n")
        #print(qeq)
        qeq = qeq[3].replace("Unnamed: 3", "").replace(" ", "")
        #print(qeq)
        qeq = float(qeq)
        if int(qeq) >= 19:
            res = "Много"
            #return res
        elif int(qeq) >= 10:
            res = "Достаточно"
            #return res
        elif int(qeq) >= 6 and int(qeq) <= 9:
            res = "Торопись"
            #return res
        elif int(qeq) >= 1 and int(qeq) <= 5:
            res = "Мало"
            #return res
        elif int(qeq) == 0:
            res = "Отсутствует"
            for i in range(1, 28):
                q = qss.get(str(i))
                upq = len(q)
                for e in range(0, upq):
                    alt = q[e]
                    if alt in q:
                        if res == "Много" or res == "Достаточно" or res == "Торопись" or res == "Мало":
                           print("нашел прерываю")
                           break
                        else:
                            dfa = pd.read_excel("C:\\task\\ostatki.xls")
                            df_abcd = dfa[dfa["Артикул"] == alt]
                            for rowa in df_abcd.iterrows():
                                alta = str(rowa)
                                alta = alta.split("\n")
                                # qeq = qeq
                                alta = alta[3].replace("Unnamed: 3", "").replace(" ", "")
                                alta = float(alta)
                                print(alt, alta)
                                if int(alta) == 0:
                                    res = "Отсутствует"
                                    print(alt, res)
                                    break
                                else:
                                    if int(alta) >= 19:
                                        res = "Много"
                                        # upq = 0
                                        print(res)
                                        break
                                    elif int(alta) >= 10:
                                        res = "Достаточно"
                                        # upq = 0
                                        break
                                    elif int(alta) >= 6 and int(qeq) <= 9:
                                        res = "Торопись"
                                        # upq = 0
                                        break
                                    elif int(alta) >= 1 and int(qeq) <= 5:
                                        res = "Мало"
                                        # upq = 0
                                        break
                    else:
                        print(alt, "no")
                break
        else:
            res = "Товара нет на складе"
            print("Tovara net")
            return res

    # print(res, str(alt))
        #await message.answer(res)
        return res, alt

# print(res + alt)
# await message.answer("Оформим?")
#     pices.append(alt)
#     print(pices)
#
#     if message.text == "да":
#         await message.answer("куда выслать заказ? вацап телега почта?")
#     else:
#         await message.answer("Подождем?")
#
# @dp.message_handler(Text(equals="да"))
# async def with_puree(message: types.Message):
#     await message.reply("qoqoqo")
#
# @dp.message_handler(lambda message: message.text == "да")
# async def echo(message: types.Message):
#     qeq = message.text
#     await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    #print(res)
