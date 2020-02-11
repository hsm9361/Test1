from flask import Blueprint, render_template

intro_blue = Blueprint('intro_blue', __name__)

# 기관소개 관련
@intro_blue.route('/way')
def way():
    html = render_template('intro/way.html')
    return html

@intro_blue.route('/hello')
def hello():
    html = render_template('intro/hello.html')
    return html