from db import database
import json

def resulvation(fr_room,fr_user_name,fr_visitors,fr_email,fr_phone,fr_hope_time,fr_hope_day):
    conn=database.get_connection()

    sql='''
        insert into facility_rental_table(fr_room,fr_user_name,fr_reservation_day,fr_visitors,
			fr_phone,fr_email,fr_hope_day,fr_hope_time)values(%s,%s,DEFAULT,%s,%s,%s,%s,%s)
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (fr_room,fr_user_name,fr_visitors,fr_phone,fr_email,fr_hope_day,fr_hope_time))
    conn.commit()
    conn.close()

def reservation_check(day,facility):
    conn = database.get_connection()

    sql = '''
            select fr_hope_time
            from facility_rental_table
            where fr_room=%s and fr_hope_day=%s
            '''
    cursor = conn.cursor()
    cursor.execute(sql, (facility,day))
    rows = cursor.fetchall()

    time_list = []
    for row in rows :
        time_list.append(row[0])

    time=json.dumps(time_list)

    return time