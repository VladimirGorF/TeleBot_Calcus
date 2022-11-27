import telebot
from random import randint


API_TOKEN = '5936246114:AAGCbe54p6aXYNxWmFa0iaKnh05wosaWSus'
bot = telebot.TeleBot(API_TOKEN)
print('Server started')
listS = [['/1', '/2', '/3'], ['/4', '/5', '/6'], ['/7', '/8', '/9']]


def Refresh():
    global listS
    listS = [['/1', '/2', '/3'], ['/4', '/5', '/6'], ['/7', '/8', '/9']]
    print(listS)


def EndGame():
    count = 0
    for i in range(3):
        for j in range(3):
            if listS[i][j] != '0' and listS[i][j] != 'X':
                count += 1
    if count == 0:
        return False


def Check_Winner():
    check = 0
    for i in range(3):
        sum = ''
        for j in range(3):
            sum += listS[i][j]
        if sum == 'XXX':
            print('Игрок победил по строкам!')
            check = 1
            break
        elif sum == '000':
            print('Компьютер победил по строкам!')
            check = 1
            break
        else:
            sum = ''
            for j in range(3):
                sum += listS[j][i]
            if sum == 'XXX':
                print('Игрок победил по столбцам!')
                check = 1
                break
            elif sum == '000':
                print('Компьютер победил по столбцам!')
                check = 1
                break

    sum = ''
    for i in range(3):
        sum += listS[i][i]
        if sum == 'XXX':
            print('Игрок победил по диагонали 1!')
            check = 1
            break
        elif sum == '000':
            print('Компьютер победил по диагонали 1!')
            check = 1
            break

    sum = ''
    i = 0
    j = 2
    while j >= 0:
        sum += listS[i][j]
        j -= 1
        i += 1
        if sum == 'XXX':
            print('Игрок победил по диагонали 2!')
            check = 1
            break
        elif sum == '000':
            print('Компьютер победил по диагонали 2!')
            check = 1
            break
    if check == 1:
        return check


def PrintGame():
    for i in range(3):
        print("  ".join(listS[i]))
    print('')


PrintGame()

@bot.message_handler(commands=['start'])
def game_message(message):
    bot.send_message(message.chat.id, f"Начинается увлекательная игра крестики-нолики! Нажмите /run для запуска")
    Refresh()

@bot.message_handler(commands=['run'])
def game_message(message):
    bot.send_message(message.chat.id, f"Смотри куда скусственный интеллект поставил 0! Он явно хочет тебя обыграть")
    i = randint(1, 3)
    j = randint(1, 3)
    while listS[i - 1][j - 1] == '0' or listS[i - 1][j - 1] == 'X':
        i = randint(1, 3)
        j = randint(1, 3)
    else:
        listS[i - 1][j - 1] = '0'
    PrintGame()
    bot.send_message(message.chat.id, f"\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")

    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Бот победил! Не отчаивайся!\nДля новой игры нажмите /start")
        Refresh()
    else:
        if EndGame() == False:
            bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
            Refresh()
        else:
            bot.send_message(message.chat.id, "Нажмите на номер ячейки, в которую ставите X.")

@bot.message_handler(commands=['1'])
def calc_message(message):
    i = 1
    j = 1
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")

@bot.message_handler(commands=['2'])
def calc_message(message):
    i = 1
    j = 2
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")

@bot.message_handler(commands=['3'])
def calc_message(message):
    i = 1
    j = 3
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")



@bot.message_handler(commands=['4'])
def calc_message(message):
    i = 2
    j = 1
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")

@bot.message_handler(commands=['5'])
def calc_message(message):
    i = 2
    j = 2
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")

@bot.message_handler(commands=['6'])
def calc_message(message):
    i = 2
    j = 3
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")

@bot.message_handler(commands=['7'])
def calc_message(message):
    i = 3
    j = 1
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")

@bot.message_handler(commands=['8'])
def calc_message(message):
    i = 3
    j = 2
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")

@bot.message_handler(commands=['9'])
def calc_message(message):
    i = 3
    j = 3
    listS[i - 1][j - 1] = 'X'
    bot.send_message(message.chat.id, f"Ваш ход\n{listS[0]}\n{listS[1]}\n{listS[2]}\n")
    if Check_Winner() == 1:
        bot.send_message(message.chat.id, "Это НЕВЕРОЯТНО!!!!  Вы победили! Получите 1 000 000 долларов США!\nДля "
                                          "новой игры нажмите /start")
        Refresh()
    elif EndGame() == False:
        bot.send_message(message.chat.id, "Игра закончена Ничьей!\nДля новой игры нажмите /start")
        Refresh()
    else:
        bot.send_message(message.chat.id, "Для хода ИИ - нажмите /run")

bot.polling()

