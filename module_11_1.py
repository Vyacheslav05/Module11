# 1. Библиотека Pillow
from PIL import Image

# Открываем изображение с помощью функции Image.open()
file_path = "leo.jpg"

try:
    with Image.open(file_path) as img:
        img.show()
except OSError as e:
    print(f"Не удалось открыть файл {file_path}: {e}")

# Переводим изображение в лругую цветовую модель с помощью метода convert()
file_path = "leo.jpg"

try:
    with Image.open(file_path) as img:
        img_gray = img.convert('L')
        img_gray.show()
        img_gray.save("leo_gray.jpg")
        # или
        img_cmyk = img.convert('CMYK')
        img_cmyk.show()
        img_cmyk.save("leo_cmyk.jpg")

except OSError as e:
    print(f"Не удалось открыть файл {file_path}: {e}")


# Изменяем размер картинки методом resize()
file_path = "leo.jpg"

try:
    with Image.open(file_path) as img:
        img_resized = img.resize((800, 600))
        img_resized.show()
        img_resized.save("leo_resized.jpg")
except OSError as e:
    print(f"Не удалось открыть файл {file_path}: {e}")

# 2. Библиотека requests
import requests

# Получаем данныe с сервера
url = 'https://api.github.com'

response = requests.get(url)
if response.status_code == 200:
    print('Данные:', response.json())
else:
    print('Ошибка:', response.status_code)

# Отправляем данные на сервер
url = 'https://api.github.com'

data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, json=data)
if response.status_code == 201:
    print('Данные созданы:', response.json())
else:
    print('Ошибка:', response.status_code)

# Обновляем данные на сервере
url = 'https://api.github.com'

data = {'key1': 'new_value1', 'key2': 'new_value2'}
response = requests.put(url, json=data)
if response.status_code == 200:
    print('Данные обновлены:', response.json())
else:
    print('Ошибка:', response.status_code)



