import pymysql
from db import database

# 세션에 따른 user_idx받기--ok
# 홈페이지에 따라 lecture_idx받기--ok
# 세션에 따라 버튼 달라지기--ok
# 드롭함수생성 인서트(신청)함수 생성 -> 디비에서 변하는지 확인--ok
# 카운트로 현재 인원수 새서 뿌리기--ok
# 신청인원이 다 차면--ok
# 강좌삭제하기 --ok (간단하게ㅠㅠ)
# 로그아웃 된 상태면 강의목록만 띄우기 -> session['login'] 사용 --ok
# 관리자권한인 친구들만 강좌등록 띄우기 --ok
# DB가 안켜져 있으면 RuntimeError: cryptography is required for sha256_password or caching_sha2_password -> pip install cryptography
# 신청기간이 지나면 버튼 사라지기

# 강좌신청가능시간을 계산하는 함수
def cal_time(lecture_idx):
    conn = database.get_connection()
    sql = '''
        select lecture_deadline
        from lecture_table
        where lecture_idx = %s
    '''
    
    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx))
    result = cursor.fetchone()
    conn.close()

    return result[0]

# 강좌를 추가하는 함수
def add_lecture(lecture_name, lecture_capacity, lecture_target, lecture_price, lecture_teacher, lecture_deadline, lecture_start, lecture_end):
    conn = database.get_connection()

    sql = '''
        insert into lecture_table(lecture_name,lecture_enrollment, lecture_capacity, lecture_target, lecture_price, lecture_teacher, lecture_deadline, lecture_start, lecture_end)
        values(%s, 0, %s, %s, %s, %s, %s, %s, %s)
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (lecture_name, lecture_capacity, lecture_target, lecture_price, lecture_teacher, lecture_deadline, lecture_start, lecture_end))
    conn.commit()
    conn.close()

def drop_lecture(lecture_idx):
    conn = database.get_connection()

    sql = '''
        delete from lecture_table
        where lecture_idx = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx))
    conn.commit()
    conn.close()



# 계정의 유형을 파악하는 함수 -> 근데 이거 user_dao.py에 있어야 하는거 아닌감.. 겹치면 삭제각
def check_user_type(user_idx):
    conn = database.get_connection()

    sql = '''
        select user_type
        from user_table
        where user_idx = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_idx))
    result = cursor.fetchone()

    conn.close()

    return result[0]


# 게시글 목록을 가져오는 함수
def get_lecture_list(page):
    # if 문 써도됨
    # page = 1
    conn = database.get_connection()

    # 현재 페이지의 글 목록의 시작 글의 인덱스
    # start_idx = (int(page) - 1) * 10


    sql = '''
        select lecture_idx, lecture_name, lecture_start, lecture_end, lecture_capacity, lecture_target, lecture_price, lecture_teacher
        from lecture_table
        limit 0, 10
    '''

    cursor = conn.cursor()
    # cursor.execute(sql, (start_idx))
    cursor.execute(sql)
    result = cursor.fetchall()

    conn.close()

    return result

# 주어진 글 번호를 통해 게시글 정보를 가져와 반환하는 함수
def get_lecture_content(lecture_idx):
    conn = database.get_connection()

    sql='''
        select lecture_idx, lecture_name, lecture_start, lecture_end, lecture_enrollment, lecture_capacity, lecture_target, lecture_price, lecture_teacher
        from lecture_table
        where lecture_idx = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx))
    result = cursor.fetchone()

    conn.close()

    return result

# 전체 글의 개수를 반환한다.
def get_total_board_cnt():
    conn = database.get_connection()

    sql = '''
        select count(*)
        from lecture
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    conn.close()
    return result[0]

# 함수 처리를 위한 사용자 정보를 가져온다.
def get_user_lecture_data(lecture_idx, user_idx):
    conn = database.get_connection()

    sql = '''
        select *
        from lecture_reservation_table
        where lecture_idx = %s and user_idx = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx, user_idx))
    result = cursor.fetchone()

    conn.close()
    return result

# 강좌 취소를 클릭시 호출되는 함수
def requested_lecture_drop(lecture_idx, user_idx):
    conn = database.get_connection()

    sql = '''
        delete from lecture_reservation_table
        where lecture_idx = %s and user_idx = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx, user_idx))
    conn.commit()
    conn.close()


# 유저가 예약 버튼을 누르면 강좌 예약 테이블에 유저의 고유번호가 추가
def reserve_lecture_user(lecture_idx, user_idx):
    conn = database.get_connection()

    sql = '''
        insert into lecture_reservation_table(lecture_idx, user_idx, reservation_time)
        values(%s, %s, sysdate())
    '''
    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx, user_idx))
    conn.commit()
    conn.close()

# 카운트로 현재 인원수 새서 뿌리기
def count_lecture_user(lecture_idx):
    conn = database.get_connection()
    
    sql = '''
        select count(*)
        from lecture_reservation_table
        where lecture_idx = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx))
    result = cursor.fetchone()

    conn.close()
    return result
