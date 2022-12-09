from flask import Blueprint, render_template, request
import functions

#  создаем блюпринт
main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')

@main_blueprint.route("/")
def main():
    #  выводим страницу
    return render_template("index.html")


@main_blueprint.route("/search")
def search():
    #  реализуем поиск ключевого слова в описаниях к постам
    s = request.args.get('s')    #  вынимаем ключевое слово из формы поиска
    posts = functions.search(s)     #  список постов с ключевым словом
    count = int(len(posts))    #  проверка на наличие совпадений

    #  возвращаем шаблон с полученными данными
    return render_template("post_list.html", s=s.lower(), posts=posts, count=count)
