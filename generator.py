# Импорт библиотеки OpenAi
import openai

# Присвоила переменной ключ API от OpenAI
openai.api_key = "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"

# importing other libraries
import requests
from PIL import Image


# Функция для генерации изображения по тексту
def generate(text):
    res = openai.Image.create(
        # текстовый запрос, по которому генерируется иображение
        prompt=text,
        # количество изображения для генерации
        n=1,
        # размер сгенерированного изображения
        size="256x256",
    )
    return res["data"][0]["url"]


# Запрос желаемого изображения
text = "bouquet of flowers"
# Цикл для генерации 40 изображений
for i in range(40):
    # Вызов функции generate с аргументом text
    # Присваивание полученного url переменной url1
    url1 = generate(text)
    # Использование библиотеки requests для преобразования image в Bytes
    response = requests.get(url1, stream=True)
    # Дублирование для коныертации в RGB
    response1 = requests.get(url1, stream=True)
    # Конвертация изображения bytes в RGB
    img = Image.open(response1.raw).convert("RGB")
    # Получение значений red, gree, blue изображения
    r, g, b = img.getpixel((1, 1))
    # Условие для rgb с целью сохранения изображений в определенной цветовой гамме(красно-желто-оранжевой)
    if (r >= 50 and r <= 255) and (g >= 50 and g <= 255) and (b >= 0 and b <= 150):
        # Сохранение изображения в формате png
        with open(f"img_gen/a_{i}.png", "wb") as f:
            f.write(response.content)
