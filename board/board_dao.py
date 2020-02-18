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