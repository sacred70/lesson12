import json
from json import JSONDecodeError

POST_PATH = "posts.json"

def get_posts_all(POST_PATH=POST_PATH):
    #  чтение файла, возвращаем список
    try:

        with open(POST_PATH, "r", encoding='utf-8') as f:
            text = json.load(f)
            return text
    except FileNotFoundError:
        # Будет выполнено, если файл не найден
        return "Файл не найден"
    except JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        return "Файл не удается преобразовать"
#print(get_posts_all())


def search(key_search):
    #  поиск ключевого слова в описании постов
    list_posts = get_posts_all()  #  загоняем список в переменную
    posts=[]
    for post in list_posts:
        if key_search in post['content']:
            posts.append(post)  #  собираем словарь с совпавшими постами
    return posts

#print(search("что"))

def loader_in_file(url, content):
    file_type = url.split('.')[-1]
    if file_type not in ["jpg", "jpeg", "png"]:
        return "Этот файл не картинка"

    json_data = [{"pic": url, "content": content}]
    with open(POST_PATH, "w") as file:
        file.write(json.dump(json_data, ensure_ascii=False))
