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
while len(promo_codes) < 1000:
    part1 = generate_random_part(4)
    part2 = generate_random_part(3)
    promo_code = f"SCX-RED-2024-{part1}-{part2}"
    if promo_code not in used_codes:  # Проверка на уникальность
        promo_codes.add(promo_code)

promo_codes = list(promo_codes)

# Путь к изображению для проверки
image_path = 'C:/Users/zxacs/Pictures/Screenshots/q.PNG'  # Замените на путь к вашему изображению

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
        time.sleep(0.00001)

        pyautogui.write(promo_code)
        time.sleep(0.00001)

        # Нажимаем Enter
        pyautogui.press('enter')
        time.sleep(0.00001)

        # Проверка наличия изображения на экране после нажатия Enter
        if check_image_on_screen(image_path):
            pyautogui.moveTo(935, 603, duration=0.00001)
            pyautogui.click()
            time.sleep(0.00001)

            print(f"Промокод {promo_code} успешно введён.")
            
            # Добавляем промокод в список использованных
            used_codes.add(promo_code)
        else:
            print("Изображение не найдено на экране после нажатия Enter. Пропускаем дальнейшие действия.")

    except Exception as e:
        print(f"Ошибка при вводе промокода {promo_code}: {e}")

# Сохранение использованных промокодов перед завершением
save_used_codes(used_codes)