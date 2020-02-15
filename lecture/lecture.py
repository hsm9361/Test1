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
    print(lecture_idx)
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

# 게시글 작성 페이지
@lecture_blue.route('/lecture_write')
def lecture_write():
    # 파라미터 데이터 추출
    html = render_template('lecture/lecture_write.html')
    return html

# 게시글 수정 페이지
# @lecture_blue.route('/lecutre_modify')
# def lecture_modify():
# 
#     data_dic = {
#         "board_writer_name" : "홍길동",
#         "board_subject" : "글 제목입니다_홍길동",
#         "board_content" : "글 내용입니다_홍길동",
#         "board_image" : "image/aaaa.jpg"
#     }
#     html = render_template('lecture/lecture_modify.html',data_dic=data_dic)
#     return html

# 글쓰기 처리 페이지
# @board_blue.route('/board_writer_pro', methods=['post'])
# def board_writer_pro():
#     # 파라미터 데이터 추출
#     board_info_idx = request.values.get('board_info_idx')
#     board_writer_idx = session['user_idx']
#     board_subject = request.values.get('board_subject')
#     board_content = request.values.get('board_content')
# 
#     # 업로드 된 파일이 있다면
#     # 첨부파일을 설정했다면 name 속성의 값을 이름으로해서 전달된다.
#     if 'board_image' in request.files:
#         # 파일 데이터를 추출한다.
#         board_image = request.files['board_image']
#         # 저장할 파일 이름 (중복을 방지하기 위해 시간데이터 사용)
#         file_name = str(int(time.time())) + board_image.filename
#         # 저장될 경로를 합친 이름을 만든다.
#         file_path = os.getcwd() + '/static/image/'+file_name
#         # 저장한다.
#         board_image.save(file_path)
#     else :
#         file_name = None
# 
#     # 저장
#     board_idx = board_database.add_board_content(board_subject, board_content, board_writer_idx, board_info_idx, file_name)
# 
#     return f'''
#         <script>
#             alert('작성이 완료되었습니다.')
#             location.href='board_read?board_idx={board_idx}'
#         </script>
#     '''

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
#
