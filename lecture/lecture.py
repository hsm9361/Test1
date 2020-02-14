from flask import Blueprint, render_template

lecture_blue = Blueprint('lecture_blue', __name__)

# 강의리스트보는함수
@lecture_blue.route('/lecture_list')
def lecture_list():
    html = render_template('lecture/lecture_list.html')
    return html

# 강의내용보는함수
@lecture_blue.route('/lecture_join')
def lecture_read():
    html = render_template('lecture/lecture_join.html')
    return html
