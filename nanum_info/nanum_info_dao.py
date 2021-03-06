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
    
def support(support_name, support_gender, support_birthday, support_email, support_phone,
            support_address, support_type, support_content, support_range, support_method,
            support_donation, support_account, support_account_name, support_bank_name, support_withdrawal):
    conn = database.get_connection()
    
    sql='''
        insert into support_table(support_name, support_gender, support_birthday, support_email,
						support_phone, support_address, support_type, support_content,
                        support_range, support_method, support_donation, support_account,
                        support_account_name, support_bank_name, support_withdrawal)
                        values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

    cursor = conn.cursor()
    cursor.execute(sql, (support_name, support_gender, support_birthday, support_email, support_phone,
            support_address, support_type, support_content, support_range, support_method,
            support_donation, support_account, support_account_name, support_bank_name, support_withdrawal))
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

def get_reservation_list():
    conn = database.get_connection()

    sql = '''
                select f.fr_idx, r.room_name, f.fr_user_name, f.fr_visitors,f.fr_hope_day, t.fr_time, f.fr_reservation_day
                from facility_rental_table f
                    inner join fr_time_table t
                    on f.fr_hope_time=t.fr_time_idx
                    inner join room_type_table r
                    on f.fr_room=r.room_idx
                    order by f.fr_hope_day
                '''
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    conn.close()

    return result

