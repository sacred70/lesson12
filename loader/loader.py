from flask import Blueprint, render_template, request
import functions

#  создаем блюпринт
loader_bueprint = Blueprint("loader_bueprint", __name__, template_folder='templates')

@loader_bueprint.route("/post", methods=["GET", "POST"])
#  переходим на страницу добавления поста
def loader():
    return render_template("post_form.html")

@loader_bueprint.route("/post", methods=["POST"])
def post_losder():
    #  проверка на внесение данных
    pic = request.files("pic")
    content = request.form("content")
    file_name = pic.filename
    pic.save(f"./uploads/{file_name}")
    if not pic or not content:
        return "error loader"
