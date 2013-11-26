# -*- coding: utf-8 -*-
"""
Defines views.
"""

from flask import render_template

from .main import app
from .utils import jsonify

import logging
log = logging.getLogger(__name__)  # pylint: disable-msg=C0103


@app.route('/')
def main_page():
    """
    Show main page.
    """
    return render_template('main.html')


@app.route('/api/v1/upload', methods=['POST'])
@jsonify
def upload():
    """
    Saves image for later use, generate thumbnail.
    """
    return {'img_id': ''}


@app.route('/api/v1/exif/<int:img_id>', methods=['GET'])
@jsonify
def exif(img_id):
    """
    Returns EXIF data of uploaded image.
    """
    return {}


@app.route('/api/v1/thumb/<int:img_id>', methods=['GET'])
@jsonify
def thumb(img_id):
    """
    Returns thumbnail of uploaded image.
    """
    return {}


