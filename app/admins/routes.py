from crypt import methods
from flask import redirect, url_for, render_template,request, flash, Blueprint
from app import db
from app.models import Tattoo, Post
from app.admins.forms import PostForm, TattooForm
from app.admins.utils import save_picture

admins = Blueprint("admins", __name__)

@admins.route('/admin')
def admin_home():
    return render_template('admin_layout.html')


@admins.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        image_file=save_picture(form.image.data)
        post = Post(title=form.title.data, content=form.content.data, 
        image=image_file)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("admins.admin_home"))
    return render_template("create_post.html", form=form)


@admins.route('/create_tattoo', methods=['POST', 'GET'])
def create_tattoo():
    form = TattooForm()
    if form.validate_on_submit():
        if form.image.data:
            image_file = save_picture(form.image.data)
            tattoo = Tattoo(name=form.name.data, image=image_file)
            db.session.add(tattoo)
            db.session.commit()
            flash("Tattoo has been successfully uploaded", "success")
        return redirect(url_for("admins.create_tattoo"))
    return render_template("create_tattoo.html", form=form)