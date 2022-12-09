from flask import Blueprint, render_template, request
import functions

#  создаем блюпринт
loader_bueprint = Blueprint("loader_bueprint", __name__, template_folder='templates')

@loader_bueprint.route("/post")
#  переходим на страницу добавления поста
def loader():
    return render_template("post_form.html")

def post_losder():
    #  проверка на внесение данных
    pic = request.files.get("pic")
    content = request.form.get("content")
    if not pic or not content:
        return "error loader"
