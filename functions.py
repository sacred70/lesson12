import json
from json import JSONDecodeError
import logging

POST_PATH = "posts.json"
logging.basicConfig(filename="basic2.log", level=logging.INFO)


def get_posts_all(POST_PATH=POST_PATH):
    #  чтение файла, возвращаем список
    try:
        with open(POST_PATH, "r", encoding='utf-8') as f:
            text = json.load(f)
            return text

    except FileNotFoundError:
        # Будет выполнено, если файл не найден
        print ("Файл не найден")

    except JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        print("Файл не удается преобразовать")


def search(key_search):
    #  поиск ключевого слова в описании постов

    list_posts = get_posts_all()  #  загоняем список в переменную
    posts = []
    for post in list_posts:
        logging.info("Выполняется поиск")
        if key_search in post['content']:
            posts.append(post)  #  собираем словарь с совпавшими постами
    return posts


def loader_in_file(url, content, file_name):
    file_type = file_name.split('.')[-1]
    print(file_type)
    json_data = {"pic": url, "content": content}
    with open(POST_PATH, "r", encoding='utf-8') as f:
        text = json.load(f)
    text.append(json_data)
    with open(POST_PATH, "w", encoding='utf-8') as t:
        json.dump(text, t, ensure_ascii=False, indent=2)
