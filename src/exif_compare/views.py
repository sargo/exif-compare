# -*- coding: utf-8 -*-
"""
Defines views.
"""
import re
import os.path
import subprocess

from flask import render_template, request
from werkzeug import secure_filename

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


def get_file_size(file):
    file.seek(0, 2) # Seek to the end of the file
    size = file.tell() # Get the position of EOF
    file.seek(0) # Reset the file position to the beginning
    return size


@app.route('/api/v1/upload', methods=['POST'])
@jsonify
def upload():
    """
    Saves image for later use, generate thumbnail.
    """
    result = {}

    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            fullfn = os.path.join(app.config['TMP_DIR'], filename)
            file.save(fullfn)

            result['name'] = os.path.basename(file.filename)
            result['type'] = file.content_type
            result['size'] = get_file_size(file.stream)
            result['exif'] = get_exif(fullfn)

            os.remove(fullfn)

    return result


def get_exif(filename):
    """
    Returns EXIF data of uploaded image.
    """
    cmd = [app.config['EXIV2_EXE'], '-ps', filename]
    try:
        output = subprocess.check_output(cmd)
    except subprocess.CalledProcessError, e:
	output = e.output

    result = []
    for i, line in enumerate(output.split('\n')):
        if i == 0:
            line = line.replace(app.config['TMP_DIR']+'/', '')
        sep = line.find(':')
        if sep >= 0:
            result.append([line[:sep].strip(), line[sep+1:].strip()])

    cmd = [app.config['EXIV2_EXE'], '-pt', filename]
    try:
        output = subprocess.check_output(cmd)
    except subprocess.CalledProcessError:
        return result

    for line in output.split('\n'):
        parts = line.split()
        if len(parts) >= 4:
            value = ' '.join(parts[3:])
            if len(value) > 100:
                value = value[:100] + '...'
            result.append([parts[0], value])
        elif len(parts) >= 1:
            result.append([parts[0], ''])

    return result
