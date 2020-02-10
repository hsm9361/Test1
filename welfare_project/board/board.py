from flask import Blueprint, render_template

board_blue = Blueprint('board_blue', __name__)

# 게시판목록
@board_blue.route('/board_list')
def board_list():
    html = render_template('board/board_list.html')
    return html