from db import database
import requests
import json

# 회원가입을 하는 함수
def add_user(user_name,user_id,user_pw,user_email):
    conn=database.get_connection()

    sql='''
        insert into user_table(user_id, user_pw, user_email, user_name, user_type)
        values(%s,%s,%s,%s,%s)
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_id,user_pw,user_email,user_name,'A'))
    conn.commit()
    conn.close()


# 카카오톡 회원가입
def add_user_kakao(user_name,user_id,user_pw,user_email, user_kakao_idx):
    conn=database.get_connection()

    sql='''
        insert into user_table(user_id, user_pw, user_email, user_name, user_type, user_kakao_idx)
        values(%s,%s,%s,%s,%s,%s)
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_id,user_pw,user_email,user_name,'A', user_kakao_idx))
    conn.commit()
    conn.close()

# 카카오톡 유저 체크하는 함수
def kakao_user_check(user_kakao_idx):
    conn=database.get_connection()

    sql='''
        select user_kakao_idx
        from user_table
        where user_kakao_idx=%s
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_kakao_idx))
    result = cursor.fetchone()
    if result == None:
        conn.close()
        return 'No'
    else:
        user_kakao_idx = result[0]
        conn.close()
        return user_kakao_idx


# 카카오톡 로그인
def user_kakao_login(headers):
    url = "https://kapi.kakao.com/v2/user/me"
    response = requests.request("POST", url, headers=headers)
    kakao_id_json = json.loads(((response.text).encode('utf-8')))  # 카카오 로그인 회원 id json
    user_kakao_idx = kakao_id_json["id"]  # 카카오 로그인 회원 id (string)
    user_id_chk = kakao_user_check(user_kakao_idx)
    if user_id_chk == user_kakao_idx:
        return True
    else:
        return False
    
def user_kakao_user_id(headers):
        url = "https://kapi.kakao.com/v2/user/me"
        response = requests.request("POST", url, headers=headers)
        kakao_id_json = json.loads(((response.text).encode('utf-8')))  # 카카오 로그인 회원 id json
        user_kakao_idx = kakao_id_json["id"]  # 카카오 로그인 회원 id (string)
        conn = database.get_connection()

        sql = '''
            select user_name
            from user_table
            where user_kakao_idx=%s 
            '''

        cursor = conn.cursor()
        cursor.execute(sql, user_kakao_idx)

        result = cursor.fetchone()
        return result[0]

# 로그인 체크하는 함수
def login_check(user_id,user_pw):
    conn=database.get_connection()

    sql='''
        select user_idx, user_pw, user_type, user_name
        from user_table
        where user_id=%s and user_pw=%s
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_id,user_pw))

    result = cursor.fetchone()
    print(result)
    if result == None :
        conn.close()
        return 'No'
    else :
        conn.close()
        return result




def user_kakao_insert(headers):
    # 카카오 DB 저장
    url = "https://kapi.kakao.com/v1/user/signup"
    response = requests.request("POST", url, headers=headers)
    # DB에 user정보 저장
    url = "https://kapi.kakao.com/v2/user/me"
    response = requests.request("POST", url, headers=headers)

    kakao_id_json = json.loads(((response.text).encode('utf-8')))  # 카카오 로그인 회원 id json
    kakao_user_json = json.loads(((response.text).encode('utf-8')))['kakao_account']  # 카카오 로그인 회원 email json

    kakao_dict = {}
    kakao_dict['user_kakao_idx'] = kakao_id_json["id"] # 카카오 로그인 회원 id
    kakao_dict['user_kakao_email'] = kakao_user_json["email"]  # 카카오 로그인 회원 email



    return kakao_dict






def email_check(email):
    conn = database.get_connection()

    sql = '''
            select user_name
            from user_table
            where user_email=%s
            '''

    cursor = conn.cursor()
    cursor.execute(sql, (user_email))

    result = cursor.fetchone()
    print(result)
    if result == None:
        conn.close()
        return 'No'
    else:
        conn.close()
        return result