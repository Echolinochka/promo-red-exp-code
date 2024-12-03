Этот код будет генерировать 100 штук промокодов естсественно он будет их подбирать и вариаций более и менее 70 миллионов но всё же правильный найти можно. И так как он работает заходим в игру STALCRAFT X заходим в меню в свой профиль там где надо активировать промокод и ничего не делаем просто запускаем код. И так курсор мышки будет наводиться на кнопку АКТИВИРОВАТЬ ПРОМОКОД сам  кликать ЛКМ потом он копирует сгенерированный код ВСТАВЛЯЕТ ЕГО и нажимает сам на ENTER потом он сам наводиться и нажимает на кнопку продолжить и так далее по новой коды он вводит разные но тем не менее правильный найти можно. УДАЧИ В НАХОДКЕ РАБОТАЮЩЕГО ПРОМОКОДА. САМОЕГО ГЛАВНОЕ ВАША РАСКЛАДКА КЛАВИАТУРЫ ДОЛЖНА БЫТЬ НА ЛАТИНСКОМ ТО ЕСТЬ НА АНГЛИЙСКОМ ЕСЛИ БУДЕТ НА РУССКОМ ТО КОД БУДЕТ ВСТАВЛЯТЬ ТОЛЬКО ТИРЕ И ЦИФРЫ 

-в новой выресии 1.1
-добавлен соврадение скрина тоесть надо скачать скрин и указать путь к этому скрину при введение промокода код будет искать этот скрин если найден то продолжит это сделано из за того что скорость слишком большая и он иногда скипает некоторые промокоды 
-добавлен функционал остановки скрипта при зажатии клавиши (ctrl или z) после чего он остановиться
-добавлено создание текстового документа если его нету то ничего страшного он сам создат в директории где и находиться сам скрипт в этот документ он будет вписывать промокоды которые уже введены что бы их не повторять это увеличивает с каждым введеным промокодом шанс найти работающий 
-ИСПРАВЛЕНО код я брал у чувака одного и там прикол был что он генерирует последние 4 и 4 символа рандом но я заметил что в промокодах от STALCRAFT идет комбинация не последние SCX-RED-2024-XXXX-YYYY а идет SCX-RED-2024-XXXX-YYY то есть 4 и 3 так что теперь вполне правильно будет вводить их




import random
import string
import pyautogui
import time
import keyboard
import os
import cv2
import numpy as np

# Имя файла для хранения использованных промокодов
USED_CODES_FILE = 'used_codes.txt'

def load_used_codes():
    """Загрузить использованные промокоды из файла."""
    if os.path.exists(USED_CODES_FILE):
        with open(USED_CODES_FILE, 'r') as f:
            return set(line.strip() for line in f)
    return set()

def save_used_codes(used_codes):
    """Сохранить использованные промокоды в файл."""
    with open(USED_CODES_FILE, 'w') as f:
        for code in used_codes:
            f.write(code + '\n')

def generate_random_part(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def check_image_on_screen(image_path):
    """Проверить, есть ли изображение на экране."""
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

    # Загружаем изображение для проверки
    template = cv2.imread(image_path)
    result = cv2.matchTemplate(screenshot_cv, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.4  # Порог для совпадения

    # Проверяем совпадение
    loc = np.where(result >= threshold)
    return loc[0].size > 0  # Возвращаем True, если изображение найдено

# Загрузка использованных промокодов
used_codes = load_used_codes()

promo_codes = set()
while len(promo_codes) < 100:
    part1 = generate_random_part(4)
    part2 = generate_random_part(3)
    promo_code = f"SCX-RED-2024-{part1}-{part2}"
    if promo_code not in used_codes:  # Проверка на уникальность
        promo_codes.add(promo_code)

promo_codes = list(promo_codes)

# Путь к изображению для проверки
image_path = 'путь к вашей фотографии по которой код будет искать скрин совпадении что бы продолжить'  # Замените на путь к вашему изображению

for promo_code in promo_codes:
    try:
        if keyboard.is_pressed('esc'):
            print("Скрипт остановлен пользователем.")
            break

        if keyboard.is_pressed('ctrl') or keyboard.is_pressed('z'):
            print("Скрипт остановлен по нажатию клавиши 'ctrl' или 'z'.")
            break

        pyautogui.moveTo(404, 830, duration=0.00001)
        pyautogui.click()
        time.sleep(0.001)

        pyautogui.write(promo_code)
        time.sleep(0.001)

        # Нажимаем Enter
        pyautogui.press('enter')
        time.sleep(0.001)

        # Проверка наличия изображения на экране после нажатия Enter
        if check_image_on_screen(image_path):
            pyautogui.moveTo(935, 603, duration=0.001)
            pyautogui.click()
            time.sleep(0.001)

            print(f"Промокод {promo_code} успешно введён.")
            
            # Добавляем промокод в список использованных
            used_codes.add(promo_code)
        else:
            print("Изображение не найдено на экране после нажатия Enter. Пропускаем дальнейшие действия.")

    except Exception as e:
        print(f"Ошибка при вводе промокода {promo_code}: {e}")

# Сохранение использованных промокодов перед завершением
save_used_codes(used_codes)

        print(f"Промокод {promo_code} успешно введён.")

    except Exception as e:
        print(f"Ошибка при вводе промокода {promo_code}: {e}")
