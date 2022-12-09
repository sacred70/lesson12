import json

POST_PATH = "posts.json"

def get_posts_all(POST_PATH=POST_PATH):
    with open(POST_PATH, "r", encoding='utf-8') as f:
        text = json.load(f)
        return text
#print(get_posts_all())


def search(key_search):
    list_posts = get_posts_all()
    posts=[]
    for post in list_posts:
        if key_search in post['content']:
            posts.append(post)
    return posts

#print(search("что"))

