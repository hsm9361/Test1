from flask import Blueprint, render_template

board_blue = Blueprint('board_blue', __name__)

# 공지사항 목록
@board_blue.route('/board_list')
def board_list():
    html = render_template('board/board_list.html')
    return html

# 공지사항 보기
@board_blue.route('/board_read')
def board_read():
    html = render_template('board/board_read.html')
    return html

# 공지사항 쓰기
@board_blue.route('/board_write')
def board_write():
    html = render_template('board/board_write.html')
    return html

# 공지사항 수정
@board_blue.route('/board_modify')
def board_modify():
    html = render_template('board/board_modify.html')
    return html

# 자유게시판 목록
@board_blue.route('/free_list')
def free_list():
    html = render_template('board/free_list.html')
    return html

# 자유게시판 글쓰기
@board_blue.route('/free_write')
def free_write():
    html = render_template('board/free_write.html')
    return html

# 자유게시판 수정하기
@board_blue.route('/free_modify')
def free_modify():
    html = render_template('board/free_modify.html')
    return html

# 자유게시판 보기
@board_blue.route('/free_read')
def free_read():
    html = render_template('board/free_read.html')
    return html
