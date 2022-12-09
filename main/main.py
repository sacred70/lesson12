from flask import Blueprint, render_template, request
import functions

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')

@main_blueprint.route("/")
def main():
    return render_template("index.html")


@main_blueprint.route("/search")
def search():
    s = request.args.get('s')
    posts = functions.search(s)
    count = int(len(posts))

    return render_template("post_list.html", s=s.lower(), posts=posts, count=count)
