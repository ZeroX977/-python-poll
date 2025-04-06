import time

vopros1 = " Ты опять просидел все дни каникул в деревне?"
vopros2 = " Ты опять профукал все каникулы?"
vopros3 = " Когда хочешь что-то начать, сразу бросаешь?"
vopros4 = " В любую свободную минуту смотришь ТТ (ТикТок)?"
vopros5 = " Ешь что попало?"
vopros6 = " Снова ничего не делал на каникулах?"
DorogoiDnevnik = " Дорогой дневник! Мне не описать боль и унижения которые я сейчас испытал..."

Error120 = "Error 120 - Ошибка ввода, вопрос не был записан в базу данных!"

DaOrNet = " (Пиши только: Da или Net, по английски иначе будет ошибка!)"
nextVopros = " Следующий вопрос:"
timer = 60
timerExit = "Сейчас вы можете закрыть программу, или она сома закроется через 30 секунд! Пока!"

print("Привет! Я твой виртуальный психолог! Давай начнём! Сейчас я задам тебе пару вопросов!")
time.sleep(5)
print("Ну чтош, вот и первый вопрос!")
time.sleep(3)
print("Вопрос №1:" + vopros1 + DaOrNet)
otvet = input()
if otvet == "Da":
    print("Ок" + nextVopros)
else:
    print(Error120)
    time.sleep(3)
    print("Ок" + nextVopros)
time.sleep(3)
print("Вопрос №2:" + vopros2 + DaOrNet)
otvet = input()
if otvet == "Da" and "Net":
    print("Ок" + nextVopros)
else:
    print(Error120)
    time.sleep(3)
    print("Ок" + nextVopros)
time.sleep(3)
print("Вопрос №3:" + vopros3 + DaOrNet)
otvet = input()
if otvet == "Da" and "Net":
    print("Ок" + nextVopros)
else:
    print(Error120)
    time.sleep(3)
    print("Ок" + nextVopros)
time.sleep(3)
print("Вопрос №4:" + vopros4 + DaOrNet)
otvet = input()
if otvet == "Da" and "Net":
    print("Ок" + nextVopros)
else:
    print(Error120)
    time.sleep(3)
    print("Ок" + nextVopros)
time.sleep(3)
print("Вопрос №5:" + vopros5 + DaOrNet)
otvet = input()
if otvet == "Da" and "Net":
    print("Ок" + nextVopros)
else:
    print(Error120)
    time.sleep(3)
    print("Ок" + nextVopros)
time.sleep(3)
print("Вопрос №6:" + vopros6 + DaOrNet)
otvet = input()
if otvet == "Da" and "Net":
    print("Ок" + nextVopros)
else:
    print(Error120)
    time.sleep(3)
    print("Ок" + nextVopros)
time.sleep(3)
print("Чтош все вопросы закончились!")
time.sleep(3)
print("Сбор ответов на вопросы...")
time.sleep(5)
print("Почти готово...")
time.sleep(5)
print("Готово!, через 5 секунд будет твой результат!")
time.sleep(5)
print(DorogoiDnevnik)
time.sleep(3)
print(timerExit)
time.sleep(30)
exit
