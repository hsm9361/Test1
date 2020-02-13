from flask import Blueprint, render_template
user_blue = Blueprint('user_blue', __name__)

@user_blue.route('/log_in')
def log_in():
    html = render_template('user/log_in.html')
    return html

@user_blue.route('/mypage')
def mypage():
    html = render_template('user/mypage.html')
    return html

@user_blue.route('/user_join')
def join():
    html = render_template('user/user_join.html')
    return html