from flask import Blueprint, render_template, request
from functions import loader_in_file
import logging


#  создаем блюпринт
loader_bueprint = Blueprint("loader_bueprint", __name__, template_folder='templates')
logging.basicConfig(filename="basic1.log", level=logging.ERROR)


@loader_bueprint.route("/post", methods=["GET", "POST"])
#  переходим на страницу добавления поста
def loader():
    return render_template("post_form.html")


@loader_bueprint.route("/upload", methods=["POST"])
def post_loader():
    #  проверка на внесение данных, запись в json, переход в форму
    #if request.method == 'POST':
    pic = request.files["picture"]
    content = request.form["content"]
    file_name = pic.filename
    if file_name not in ["jpg", "jpeg", "png"]:
        logging.info("Неверный тип файла")
        return "Этот файл не картинка"
    url = f"./uploads/{file_name}"
    if not pic or not content:
        logging.error("Данные не загружены")
        return "Заполнены не все поля"


    pic.save(url)
    loader_in_file(url, content, file_name)

    return render_template("post_uploaded.html", url=url, text=content)


