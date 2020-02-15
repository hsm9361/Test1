import pymysql
from db import database

# 강좌 정보를 보여주는 함수 => 그냥 DB에서 가져오면 된다.
# 변경되는 사항을 함수 만들기

# 디비에서 불러오기
# 강좌신청 인원이 모두 차면 버튼 사라지기
# 강좌 신청 기간이 지나면 버튼 사라지기
# 강좌 취소 버튼 생성 -> 데이터베이스에서 drop
# 예약 했을 때만 취소 뜨도록

# 관리자 권한만 글쓰기

# 신청받으면 db에서 len함수나 count로 인원 수 표시

# 중복확인 여부 검사
# 해당 user_idx가 같은 강의에 신청한다면 창 띄우기
# 해당 user_idx가 html에 접속한다면 버튼 띄우지 않기.


# 유저가 예약 버튼을 누르면 강좌 예약 테이블에 유저의 고유번호가 추가
def add_lecture_user(lecture_idx, user_idx):
    conn = database.get_connection()

    sql = '''
        insert into lecture_reservation_table(lecture_idx, user_idx, reservation_time)
        values(%s, %s, sysdate())
    '''
    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx, user_idx))
    conn.commit()
    conn.close()

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
    print(lecture_idx)
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
def get_user_login_data(lecture_idx, user_idx):
    conn = database.get_connection()

    sql = '''
        select lecture_idx, user_idx
        from lecture_reservation_table
        where lecture_idx = %s and user_idx = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx, user_idx))
    result = cursor.fetchone()

    conn.close()
    return result