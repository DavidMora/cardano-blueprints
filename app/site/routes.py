from flask import render_template, url_for, redirect, send_from_directory

from . import site

# custom 404 handler
@site.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@site.route('/', methods=['GET', 'POST'])
def index():
    return render_template('site/index.html')

@site.route('/public/<path:path>')
def send_js(path):
    return send_from_directory('public', path)

