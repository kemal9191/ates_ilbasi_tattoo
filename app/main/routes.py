from flask import Blueprint, jsonify, url_for, render_template, request, redirect, flash
from app.models import Tattoo, FormRequests
from app.main.forms import ContactForm
from app import db

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("main/home.html", title="Home")


@main.route('/about')
def about():
    return render_template('main/about.html',title="About")


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_request = FormRequests(title=form.subject.data, content=form.message.data)
        db.session.add(new_request)
        db.session.commit()
        flash('Mesajınız başarıyla iletildi!', 'success')
        return redirect(url_for('main.home'))
    return render_template('main/contact.html', title="Contact", form=form)


