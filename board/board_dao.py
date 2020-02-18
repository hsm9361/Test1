import pymysql
from db import database

def board_write(board_title,bc_writer_idx,board_content):
    conn = database.get_connection()

    sql = '''
            insert into board_content(bc_subject,bc_writer_idx,bc_date,bc_content,board_type_idx)
            values(%s,%s,DEFAULT,%s,1)
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (board_title,bc_writer_idx,board_content))
    conn.commit()
    conn.close()

def board_list():
    conn = database.get_connection()

    sql = '''
            select bor.bc_idx, bor.bc_subject, u.user_name, bor.bc_date, bor.bc_content 
from board_content bor
	inner join user_table u
    on bor.bc_idx = u.user_idx
where board_type_idx=1
        '''

    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    conn.close()

    return result