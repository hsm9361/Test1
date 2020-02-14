from db import database

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

# 로그인 체크하는 함수
def login_check(user_id,user_pw):
    conn=database.get_connection()

    sql='''
        select user_idx, user_pw, user_type
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
        user_idx = result[0]
        user_type = result[2]
        conn.close()
        return user_idx

