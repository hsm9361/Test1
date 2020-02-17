from flask import Blueprint, render_template, request, session
import time
import os
from lecture import lecture_dao

lecture_blue = Blueprint('lecture_blue', __name__)

# 게시글 목록 페이지
@lecture_blue.route('/lecture_list')
def lecture_list():
    # 파라미터 데이터를 추출한다.
    # 파라미터로 넘어온 데이터 값은 모두 문자열이다.
    # board_info_idx = request.values.get('board_info_idx')
    page = 0
    result = lecture_dao.get_lecture_list(page)
    
    # 게시판 이름을 가져온다.
    # board_name = board_database.get_board_info_name(board_info_idx)

    # 게시글 정보를 가져온다.

    lecture_list_data = []

    # lecture_idx, lecture_name, lecture_start, lecture_end, lecture_capacity,, lecture_target, lecture_price, lecture_teacher
    
    lecture_idx = result[0]

    # row의 수만큼 반복한다
    for row in result:
        obj = {
            'lecture_idx' : row[0],
            'lecture_name' : row[1],
            'lecture_start' : row[2],
            'lecture_end' : row[3],
            'lecture_capacity' : row[4],
            'lecture_target' : row[5],
            'lecture_price' : row[6],
            'lecture_teacher' : row[7]
        }

        lecture_list_data.append(obj)
    # html에서 사용하려면 render_template에 꼭 넣어놔야한다.
    html = render_template('lecture/lecture_list.html', lecture_list_data = lecture_list_data, lecture_idx=lecture_idx)
    return html

# 게시글 보는 페이지
@lecture_blue.route('/lecture_join/<lecture_idx>')
@lecture_blue.route('/lecture_join')
def lecture_join(lecture_idx):
    # 파라미터 데이터 추출
    # 글 정보를 가져온다.
    result = lecture_dao.get_lecture_content(lecture_idx)
    # lecture_idx, lecture_name, lecture_start, lecture_end, lecture_enrollment, lecture_capacity,
    # lecture_target, lecture_price, lecture_teacher

    data_dic = {
        "lecture_idx" : result[0],
        "lecture_name" : result[1],
        "lecture_target" : result[6],
        "lecture_teacher" : result[8],
        "lecture_enrollment" : result[4],
        "lecture_capacity" : result[5]
    }
    html = render_template('lecture/lecture_join.html',data_dic=data_dic)
    return html


# 신청 버튼 session
# @lecture_blue.route('/lecture_request', methods=['post'])
# def lecture_request():
#     user_id = request.form.get('user_id')
#     user_pw = request.form.get('user_pw')
#
#     # print(user_name,user_id,user_pw,user_email)
#     result=user_dao.login_check(user_id,user_pw)
#
#     if result == 'No' :
#         return 'NO'
#     else :
#         session['login']='YES'
#         session['user_idx'] = result
#         return 'YES'
#
#
#     # html = render_template('main/index.html')
#     # return html
#
# @user_blue.route('/user_logout')
# def user_logout():
#     session['login']=False
#     html = render_template('main/index.html')
#     return html


# 강좌 취소 처리

@lecture_blue.route('/lecture_user_drop', methods=['post','get'])
def lecture_user_drop(lecture_idx):
    lecture_idx = request.form.get(lecture_idx)
    lecture_user_idx = session['user_idx']
    
    result = lecture_dao.lecture_drop(lecture_idx,lecture_user_idx)

    html = render_template('lecture/lecture_join.html',result=result)
    return html

