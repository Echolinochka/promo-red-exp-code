import random
import string
import pyautogui
import time
import keyboard  # Не забудьте установить библиотеку keyboard

def generate_random_part(length):
    # Включаем только заглавные буквы и цифры
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Генерация 100 уникальных промокодов
promo_codes = set()  # Используем множество для уникальности
while len(promo_codes) < 100:
    part1 = generate_random_part(4)  # Первая часть
    part2 = generate_random_part(4)  # Вторая часть
    promo_code = f"SCX-RED-2024-{part1}-{part2}"  # Форматирование промокода
    promo_codes.add(promo_code)

# Преобразуем множество в список для упрощения обработки
promo_codes = list(promo_codes)

# Обработка каждого промокода
for promo_code in promo_codes:
    try:
        # Проверка нажатия клавиши Esc
        if keyboard.is_pressed('esc'):
            print("Скрипт остановлен пользователем.")
            break

        # Перемещение курсора на координаты (404, 830) и клик
        pyautogui.moveTo(404, 830, duration=0.5)  # Перемещение с задержкой
        pyautogui.click()  # Клик ЛКМ
        time.sleep(0.5)  # Задержка после клика

        # Печатаем промокод
        pyautogui.write(promo_code)
        time.sleep(0.5)  # Задержка перед нажатием Enter
        pyautogui.press('enter')  # Нажимаем Enter
        time.sleep(1)  # Задержка перед следующим действием

        # Перемещение курсора на координаты (935, 603) и клик
        pyautogui.moveTo(935, 603, duration=0.5)  # Перемещение с задержкой
        pyautogui.click()  # Клик ЛКМ
        time.sleep(1)  # Задержка перед следующим циклом

        print(f"Промокод {promo_code} успешно введён.")

    except Exception as e:
        print(f"Ошибка при вводе промокода {promo_code}: {e}")