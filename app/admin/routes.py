from crypt import methods
from inspect import CO_ASYNC_GENERATOR
from flask import redirect, url_for, render_template,request, flash, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import Content, Admin, FormRequests
from app.admin.forms import ContentForm, LoginForm
from app.admin.utils import save_picture
import babel

admin = Blueprint("admin", __name__)


@admin.route('/admin', methods=['GET', 'POST'])
@admin.route('/admin/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.add_content'))
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(name=form.username.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin.add_content'))
        else:
            flash('Login unsuccessful. Please check username or password', 'danger')
    return render_template('admin/login.html', form=form, title="login")


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout is successful', 'success')
    return redirect(url_for('admin.login'))


@admin.route('/admin/contents')
@login_required
def contents():
    contents = db.session.query(Content)
    return render_template('admin/contents.html', title='Galeri', contents=contents)


@admin.route('/admin/add_content', methods=['POST', 'GET'])
@login_required
def add_content():
    form = ContentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            image = save_picture(form.image.data)
            url = url_for('static', filename="images/"+image)
            content = Content(name=form.name.data, description=form.description.data,
            seo_statement=form.seo_statement.data, seo_keywords=form.seo_keywords.data,
            image=url, admin_id=current_user.id)
            db.session.add(content)
            db.session.commit()
            flash('İçerik başarıyla kaydedildi!', 'success')
            return redirect(url_for('admin.add_content'))
        else:
            flash('Girdiğiniz verileri kontrol ediniz!', 'danger')
    return render_template('admin/admin.html', title='Ekle', form=form)


@admin.route('/admin/update_content/<int:id>', methods=['POST', 'GET'])
@login_required
def update_content(id):
    form = ContentForm()
    content = Content.query.get(id)
    if request.method == 'GET':
        form.name.data = content.name
        form.description.data = content.description
        form.seo_statement.data = content.seo_statement
        form.seo_keywords.data = content.seo_keywords
    if request.method == 'POST':
        if form.validate_on_submit:
            if form.image.data:
                image = save_picture(form.image.data)
                url = url_for('static', filename="images/"+image)
                content.image = url
            content.name = form.name.data
            content.description = form.description.data
            content.seo_statement = form.seo_statement.data
            content.seo_keywords = form.seo_keywords.data
            db.session.commit()
            flash("Content has been updated!", "success")
        else:
            flash("Please check your input!")
        return redirect(url_for('admin.contents'))
    return render_template('admin/admin.html', title='Ekle', form=form)


@admin.route('/admin/delete_content/<int:id>', methods=['GET','DELETE'])
@login_required
def delete_content(id):
    content = Content.query.get(id)
    db.session.delete(content)
    db.session.commit()
    flash('İçerik başarıyla silindi!', 'success')
    return redirect(url_for('admin.contents'))


@admin.route('/admin/form_requests', methods=['GET'])
@login_required
def form_requests():
    requests = db.session.query(FormRequests)
    return render_template('admin/requests.html', title='Talepler', requests=requests)


@admin.route('/admin/form_requests/<int:id>')
@login_required
def request_details(id):
    request = FormRequests.query.get(id)
    return render_template('admin/request-detail.html', request=request, title='Talepler')


@admin.route('/admin/delete_request/<int:id>', methods=['GET','DELETE'])
@login_required
def delete_request(id):
    req = FormRequests.query.get(id)
    db.session.delete(req)
    db.session.commit()
    flash('Talep başarıyla silindi!', 'success')
    return redirect(url_for('admin.form_requests'))