from flask import Blueprint, render_template, request, session
import time
import os
from lecture import lecture_dao
# 달력을 위한 import
from datetime import datetime

lecture_blue = Blueprint('lecture_blue', __name__)


@lecture_blue.route('/lecture_write', methods=['POST','GET'])
def lecture_date():
    return render_template('/lecture/lecture_write.html')

# 게시글 추가
@lecture_blue.route('/lecture_write_pro', methods=['POST','GET'])
def lecture_write_pro():
    # 파라미터 데이터를 추출한다.
    lecture_name = request.values.get('lecture_name')
    lecture_teacher = request.values.get('lecture_teacher')
    lecture_capacity = request.values.get('lecture_capacity')
    lecture_target = request.values.get('lecture_target')
    lecture_price = request.values.get('lecture_price')
    lecture_deadline = request.form['lecture_deadline']
    # print(lecture_deadline)
    # print(type(lecture_deadline))
    lecture_start = request.form['lecture_start']
    lecture_end = request.form['lecture_end']
    # 사용자 데이터를 저장한다.
    lecture_dao.add_lecture(lecture_name, lecture_capacity, lecture_target, lecture_price, lecture_teacher, lecture_deadline, lecture_start, lecture_end)
    # 응답 결과로 가입메시지를 보여주고 첫 페이지로 이동하게 하는
    # 자바 스크립트 코드를 전달한다.
    return '''
        <script>
            alert('저장이 완료되었습니다')
            location.href='/lecture_list'
        </script>
        '''


# 게시글 목록 페이지
@lecture_blue.route('/lecture_list')
def lecture_list():
    # 파라미터 데이터를 추출한다.
    # 파라미터로 넘어온 데이터 값은 모두 문자열이다.
    # board_info_idx = request.values.get('board_info_idx')
    page = 0
    result = lecture_dao.get_lecture_list(page)

    # 유저의 타입을 받아온다.
    user_idx = session['user_idx']
    user_type = lecture_dao.check_user_type(user_idx)
    # print(user_type)
    if user_type == 'B':
        auth = True
    else :
        auth = False

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
    html = render_template('lecture/lecture_list.html', lecture_list_data = lecture_list_data, lecture_idx=lecture_idx, user_type=user_type, auth=auth)
    return html

# 게시글 보는 페이지
@lecture_blue.route('/lecture_join/<lecture_idx>')
@lecture_blue.route('/lecture_join')
def lecture_join(lecture_idx):
    # 파라미터 데이터 추출
    # 글 정보를 가져온다.
    result = lecture_dao.get_lecture_content(lecture_idx)
    reserve_count = lecture_dao.count_lecture_user(lecture_idx)

    user_idx = session['user_idx']
    request_db = lecture_dao.get_user_lecture_data(lecture_idx, user_idx)
    
    data_dic = {
        "lecture_idx" : result[0],
        "lecture_name" : result[1],
        "lecture_target" : result[6],
        "lecture_teacher" : result[8],
        "lecture_enrollment" : result[4],
        "lecture_capacity" : result[5]
    }

    # 유저타입
    user_idx = session['user_idx']
    user_type = lecture_dao.check_user_type(user_idx)
    # print(user_type)
    if user_type == 'B':
        auth = True
    else :
        auth = False
        
    # print(data_dic['lecture_capacity'])
    # print(reserve_count[0])

    # 현재 신청 인원과 전체 인원을 비교하여 bool로 리턴
    # 딕셔너리값 호출 + 튜플값 호출 => DB에서 호출되는 값은 튜플형태로 넘어온다.
    if data_dic['lecture_capacity'] == reserve_count[0] :
        current_reserve = False
    else :
        current_reserve = True

    # 세션 가져오기
    # 신청한 적이 없다면 false
    if request_db is None :
        lecture_request = False
    else:
        lecture_request = True

    # html = render_template('lecture/lecture_check.html', user_idx=user_idx, result=result)
    # return html
    html = render_template('lecture/lecture_join.html',data_dic=data_dic, lecture_request=lecture_request, user_idx=user_idx, reserve_count=reserve_count, current_reserve=current_reserve, auth=auth)
    return html

@lecture_blue.route('/delete_lecture', methods=['post'])
def delete_lecture():
    lecture_idx = request.form.get('lecture_idx')
    user_idx = session['user_idx']

    lecture_dao.requested_lecture_drop(lecture_idx, user_idx)
    return 'ok'

@lecture_blue.route('/reserve_lecture', methods=['post'])
def reserve_lecture():
    lecture_idx = request.form.get('lecture_idx')
    user_idx = session['user_idx']

    lecture_dao.reserve_lecture_user(lecture_idx, user_idx)
    # 문자라도 리턴을 하라해서..
    return 'ok'

@lecture_blue.route('/drop_lecture', methods=['post'])
def drop_lecture():
    lecture_idx = request.form.get('lecture_idx')

    lecture_dao.drop_lecture(lecture_idx)
    return 'ok'

@lecture_blue.route('/cal_time', methods=['POST'])
def cal_time():
    lecture_idx = request.form.get('lecture_idx')

    lecture_deadline = lecture_dao.cal_time(lecture_idx)
    today = datetime.today

    if today > lecture_deadline:
        time_out = True
    else :
        time_out = False

    return time_out