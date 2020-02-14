import pymysql

# 데이터베이스 접속 함수
def get_connection():
    conn=pymysql.connect(host='127.0.0.1', user='root', password='1234',
                         db='welfare', charset='utf8')
    return conn