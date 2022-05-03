from email import message
from flask import Blueprint, jsonify, url_for, render_template, request, redirect, flash
from app.models import Content, FormRequests
from app.main.forms import ContactForm
from app import db
from app.admin.utils import save_request_picture


main = Blueprint("main", __name__)

@main.route('/')
@main.route('/home')
def home():
        return render_template("main/home.html", title="Home")


@main.route('/gallery')
def gallery():
    contents = db.session.query(Content)
    return render_template('main/gallery.html', title='Gallery', contents=contents)


@main.route('/about')
def about():
    return render_template('main/about.html',title="About")


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            images = []
            for image in form.images.data:
                saved_image = save_request_picture(image)
                if saved_image:
                    url = url_for('static', filename="images/requests/"+saved_image)
                    images.append(url)
            new_request = FormRequests(name_surname=form.name_surname.data, email_address=form.email_address.data,
                        subject=form.subject.data, message=form.message.data, images=images)
            db.session.add(new_request)
            db.session.commit()
            flash('Mesajınız başarıyla iletildi!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Girdiğiniz verileri kontrol ediniz!', 'danger')
    return render_template('main/contact.html', title="Contact", form=form)



