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



    html = render_template('nanum_info/rental_ok.html')
    return html

# 예약되어있는 시간을 확인하는 함수
@nanum_info_blue.route('/facility_reservation_check/<day>/<facility>', methods=['post'])
def facility_reservation_check(day,facility):
    time=nanum_info_dao.reservation_check(day,facility)
    
    return time