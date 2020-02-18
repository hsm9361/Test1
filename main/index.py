from flask import Blueprint, render_template
from lecture import lecture_dao
from board import board_dao

main_blue = Blueprint('main_blue', __name__)

@main_blue.route('/')
def index():
    page = 0
    result = lecture_dao.get_lecture_list(page)
    content = []
    for row in result:
        obj = {
            'lecture_idx' : row[0],
            'lecture_name' : row[1]
        }
        content.append(obj)

    board = board_dao.board_list()
    board_list = []
    for row in board:
        obj = {
            'idx': row[0],
            'subject': row[1],
            'name': row[2],
            'date': row[3],
            'content': row[4]
        }
        board_list.append(obj)
    html = render_template('main/index.html',content=content,board_list=board_list)
    return html

