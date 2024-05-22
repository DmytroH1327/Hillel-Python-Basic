# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
# Ну і додатковим завданням є турбота про виведення.
# Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди повинні заповнюватися нулями при одноцифрових значеннях.
# Приклад:
# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

number = int(input("Введите номер от 0 и до 8640000: "))

a, seconds = divmod(number, 60)
b, minutes = divmod(a, 60)
days, hours = divmod(b, 24)

if days % 10 == 1 and days % 100 != 11:
    day_print = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_print = "дні"
else:
    day_print = "днів"

print(f"{days} {day_print}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
