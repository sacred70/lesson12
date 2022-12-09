import json

POST_PATH = "posts.json"

def get_posts_all(POST_PATH=POST_PATH):
    #  чтение файла, возвращаем список
    with open(POST_PATH, "r", encoding='utf-8') as f:
        text = json.load(f)
        return text
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

def loader_in_file():
    pass

