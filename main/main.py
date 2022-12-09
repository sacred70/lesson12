from flask import Blueprint, render_template, request

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')

@main_blueprint.route("/")
def main():
    return render_template("index.html")


@main_blueprint.route("/search/?s=<key_search>")
def search(key_search):
    s = request.args.get('s', "")
    return render_template("post_list.html", s=s)
