from flask import Blueprint, render_template

board_blue = Blueprint('board_blue', __name__)

# 게시판 목록
@board_blue.route('/board_list')
def board_list():
    html = render_template('board/board_list.html')
    return html

# 게시글 보기
@board_blue.route('/board_read')
def board_read():
    html = render_template('board/board_read.html')
    return html

# 게시글 쓰기
@board_blue.route('/board_write')
def board_write():
    html = render_template('board/board_write.html')
    return html

# 게시글 수정
@board_blue.route('/board_modify')
def board_modify():
    html = render_template('board/board_modify.html')
    return html