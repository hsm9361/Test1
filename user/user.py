from flask import Blueprint, render_template, request, session
from user import user_dao

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

@user_blue.route('/user_join_pro', methods=['post'])
def join_pro():
    user_name = request.form.get('user_name')
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')
    user_email = request.form.get('email')

    # print(user_name,user_id,user_pw,user_email)
    user_dao.add_user(user_name,user_id,user_pw,user_email)
    html = render_template('main/index.html')
    return html



@user_blue.route('/user_login_pro', methods=['post'])
def user_login_pro():
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    # print(user_name,user_id,user_pw,user_email)
    result=user_dao.login_check(user_id,user_pw)

    if result == 'No' :
        return 'NO'
    else :
        session['login']='YES'
        session['user_idx'] = result
        return 'YES'


    # html = render_template('main/index.html')
    # return html

@user_blue.route('/user_ouet', methods=['post'])
def user_logout():
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    # print(user_name,user_id,user_pw,user_email)
    result=user_dao.login_check(user_id,user_pw)

    if result == 'No' :
        return 'NO'
    else :
        session['login']='YES'
        session['user_idx'] = result
        return 'YES'