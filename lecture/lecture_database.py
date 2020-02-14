from db import database

# 강좌 정보를 보여주는 함수 => 그냥 DB에서 가져오면 된다.
# 변경되는 사항을 함수 만들기

# 유저가 예약 버튼을 누르면 강좌 예약 테이블에 유저의 고유번호가 추가
def add_user(lecture_idx, user_idx):
    conn = database.get_connection()

    sql = '''
        insert into lecture_reservation_table(lecture_idx, user_idx, reservation_time)
        values(%s, %s, now())
    '''
    cursor = conn.cursor()
    cursor.execute(sql, (lecture_idx, user_idx))
    conn.commit()
    conn.close()
    
# 강좌신청 인원이 모두 차면 버튼 사라지기
# 강좌 취소 버튼 생성 -> 데이터베이스에서 drop
# 관리자 권한만 글쓰기
# 신청받으면 db에서 len함수나 count로 인원 수 표시

# 중복확인 여부 검사
# 해당 user_idx가 같은 강의에 신청한다면 창 띄우기
# 해당 user_idx가 html에 접속한다면 버튼 띄우지 않기.
def check_user_id(lecture_idx, user_idx):
    conn = database.get_connection()

    sql = '''
        select * from user_table
        where user_id = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_id))
    result = cursor.fetchone()

    if result == None:   # 가져온 데이터가 없다면.
        return True
    else :
        return False

# 로그인 처리를 위한 사용자 정보를 가져온다.
def get_user_login_data(user_id, user_pw):
    conn = database.get_connection()

    sql = '''
        select user_idx, user_name
        from user_table
        where user_id = %s and user_pw = %s
    '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_id, user_pw))
    result = cursor.fetchone()

    conn.close()
    return result