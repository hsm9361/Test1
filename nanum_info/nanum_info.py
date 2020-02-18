from flask import Blueprint, render_template, request
from nanum_info import nanum_info_dao

nanum_info_blue = Blueprint('nanum_info_blue', __name__)

@nanum_info_blue.route('/volunteer')
def volunteer():
    html = render_template('nanum_info/volunteer.html')
    return html

@nanum_info_blue.route('/support')
def support():
    html = render_template('nanum_info/support.html')
    return html

@nanum_info_blue.route('/support_pro', methods=['post'])
def support_pro():
    support_name = request.form.get('sp_nm') # 후원자명
    support_gender = request.form.get('sp_gnr') # 성별

    birthday1 = request.form.get('sp_birY') # 년도
    birthday2 = request.form.get('sp_birM') # 월
    birthday3 = request.form.get('sp_birD') # 일
    support_birthday = str(birthday1) + '-' + str(birthday2) + '-' + str(birthday3)

    email1 = request.form.get('sp_email1') # email 아이디
    email2 = request.form.get('sp_email2') # email 주소
    support_email = str(email1) + '@' + str(email2)  # 합친 이메일 주소

    support_phone = request.form.get('sp_phone')  # 전화번호

    address1 = request.form.get('sp_address') # 동주소
    address2 = request.form.get('sp_detailAddress') # 상세주소
    support_address = str(address1) + " " + str(address2) # 주소

    support_type = request.form.get('sp_cgr') # 후원 종류
    support_content = request.form.get('sp_cgr_etc') # 후원 내용(지정후원의 경우)
    support_range = request.form.get('month') # 후원 기간
    support_method = request.form.get('sp_rt') # 후원 방법

    support_donation = request.form.get('sp_py') # 기부금
    support_account = request.form.get('sp_num') # 계좌
    support_account_name = request.form.get('sp_dpst') # 예금주명
    support_bank_name = request.form.get('sp_bk') # 거래은행
    support_withdrawal = request.form.get('sp_wd') # 출금일
    nanum_info_dao.support(support_name, support_gender, support_birthday, support_email, support_phone,
            support_address, support_type, support_content, support_range, support_method,
            support_donation, support_account, support_account_name, support_bank_name, support_withdrawal)



    html = render_template('nanum_info/rental_ok.html')
    return html

@nanum_info_blue.route('/facility_rental')
def facility_rental():
    html = render_template('nanum_info/facility_rental.html')
    return html

@nanum_info_blue.route('/facility_rantal_pro', methods=['post'])
def facility_rantal_pro():
    fr_room = request.form.get('rn_cgr') # 대관장소
    fr_user_name = request.form.get('rn_user') # 예약자명
    fr_visitors = request.form.get('rn_num') # 방문자수
    email1 = request.form.get('rn_email1')
    email2 = request.form.get('rn_email2')
    fr_email = str(email1)+'@'+str(email2) # 이메일 주소
    fr_phone = request.form.get('phone') # 휴대폰 번호
    fr_hope_time = request.form.get('h_time') # 희망시간대
    fr_hope_day = request.form.get('date') #예약날짜
    nanum_info_dao.resulvation(fr_room,fr_user_name,fr_visitors,fr_email,fr_phone,fr_hope_time,fr_hope_day)
    # print(f'fr_room :{fr_room} fr_user_name: {fr_user_name} fr_visitors:{fr_visitors} fr_email{fr_email} fr_phone{fr_phone}'
    #       f'fr_hope_time{fr_hope_time} fr_reservition_day{fr_reservition_day}')

    next_page = '''
        <script>
            alert('예약이 완료되었습니다.')
            location.href='/'
        </script>
        '''
    return next_page

# 예약되어있는 시간을 확인하는 함수
@nanum_info_blue.route('/facility_reservation_check/<day>/<facility>', methods=['post'])
def facility_reservation_check(day,facility):
    time=nanum_info_dao.reservation_check(day,facility)

    return time

@nanum_info_blue.route('/rental_ok')
def rental_ok():
    result=nanum_info_dao.get_reservation_list()

    data_list=[]
    for row in result :
        obj={
            'idx' : row[0],
            'room' : row[1],
            'name' : row[2],
            'visiters' : row[3],
            'day' : row[4],
            'time' : row[5],
            'reservation' : row[6]
        }
        data_list.append(obj)

    html = render_template('nanum_info/support_ok.html', data_list=data_list)
    return html