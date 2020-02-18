from flask import Blueprint, render_template, request,session
from board import board_dao
board_blue = Blueprint('board_blue', __name__)

# 공지사항 목록
@board_blue.route('/board_list')
def board_list():
    result=board_dao.board_list()
    data_list = []
    for row in result:
        obj = {
            'idx':row[0],
            'subject':row[1],
            'name':row[2],
            'date':row[3],
            'content':row[4]
        }
        data_list.append(obj)
    html = render_template('board/board_list.html',data_list=data_list)
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

# 공지사항 글쓰기 추가

@board_blue.route('/board_write_pro', methods=['post'])
def board_write_pro():
    board_title = request.form.get('board_title')  # 글제목
    board_content = request.form.get('board_content')  # 내용
    print(session)
    bc_writer_idx=session['user_idx']
    board_dao.board_write(board_title,bc_writer_idx,board_content)

    html = render_template('main/index.html')
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
