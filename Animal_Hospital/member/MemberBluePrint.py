from flask import Blueprint, render_template

member_blue=Blueprint('member',__name__)

@member_blue.route('/member_join')
def member_join ():
    html=render_template('member/member_join.html')
    return html

@member_blue.route('/member_login')
def member_login():
    html = render_template('member/member_login.html')
    return html