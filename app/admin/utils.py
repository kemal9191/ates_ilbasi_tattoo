import secrets
import os
from flask import url_for, current_app
from PIL import Image


def save_picture(tattoo_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(tattoo_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn)

    i = Image.open(tattoo_picture)
    i.save(picture_path)

    return picture_fn
