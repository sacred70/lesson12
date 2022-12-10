from flask import Blueprint, render_template, request
from functions import loader_in_file


#  создаем блюпринт
loader_bueprint = Blueprint("loader_bueprint", __name__, template_folder='templates')


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
    url = f"./uploads/{file_name}"
        #pic.save(url)
        #loader_in_file(url, content)
            #if not pic or not content:
                #return "error loader"
    return render_template("post_uploaded.html", url=url, text=content)


