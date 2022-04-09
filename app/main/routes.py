from flask import Blueprint, jsonify, url_for, render_template, request, redirect, flash
from app.models import Tattoo, FormRequests
from app.main.forms import ContactForm
from app import db

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html", title="Home")


@main.route('/about-us')
def about():
    return render_template('about.html',title="About Us")


@main.route('/gallery')
def gallery():
    tattoos = Tattoo.query.all()
    urls = []
    for tattoo in tattoos:
        url = url_for('static', filename="images/"+tattoo.image)
        urls.append(url)
    return render_template('gallery.html', title="Gallery", urls=urls)


@main.route('/contact-us', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_request = FormRequests(title=form.title.data, content=form.content.data)
        db.session.add(new_request)
        db.session.commit()
        flash('Your request has been successfully submitted', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html', title="Contact Us", form=form)


