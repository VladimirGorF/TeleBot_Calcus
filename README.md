   TeleBot_Calcus - это учебный проект Горбунова Владимира в школе Гик Брейнс на уроке по Python.
   
Проект включает в себя два различных бота:
1) Бот-калькулятор рациональных и компексных чисел.(Рациональная часть построена на базе собственного калькулятора и производит вычисления
с учетом приоритетов умножения, деления и наличия выражений в скобках.
Бот запускается командой /start, затем появляется выбор какой программой воспользоваться. При выборе команды /calcus появляется дополнительное меню 
с типом вычислений(комплексные и рациональные)
<img width="2048" alt="Снимок экрана 2022-11-24 в 22 58 27" src="https://user-images.githubusercontent.com/110591063/204153251-a3c9d290-25c1-44cd-8ecb-76b90f70e067.png">

Пример рационального калькулятора:
<img width="2048" alt="Снимок экрана 2022-11-24 в 23 02 03" src="https://user-images.githubusercontent.com/110591063/204153281-5c8d4e2d-9e67-44fe-a370-c3c47bd8bdb3.png">

Комплесные вычисления организованы с помощью встроенной функции eval.
Пример комплексных чисел:
<img width="2048" alt="Снимок экрана 2022-11-24 в 22 57 42" src="https://user-images.githubusercontent.com/110591063/204153345-2f7da612-0b52-4759-9c31-0c5699f2262e.png">

Также дополнительно реализована функция определения текущей даты и времени:
<img width="2048" alt="Снимок экрана 2022-11-24 в 22 58 10" src="https://user-images.githubusercontent.com/110591063/204153365-c5d1ba03-6f80-454a-92d9-60449fc9e6f8.png">



2) Вторая часть проекта - это известная всем игра в крестики-нолики. 

Бот запускается командой /start
Игра активируется командой /run
Первым ходит Бот. Затем пользователь нажимет на поле в котором, по его мнению, необходимо поставить Х.
<img width="2048" alt="Снимок экрана 2022-11-27 в 21 13 30" src="https://user-images.githubusercontent.com/110591063/204153560-41e8d988-5886-48df-b00c-e685060e7305.png">

Игра продолжается до победы, либо заканчивается ничьей, если полей для ввода не осталось и никто не выиграл.

В случае победы выигрыш составляет 1 млн долларов США.
<img width="2048" alt="Снимок экрана 2022-11-27 в 21 16 15" src="https://user-images.githubusercontent.com/110591063/204153681-d813f153-169e-4e83-a548-f72a78f5b118.png">