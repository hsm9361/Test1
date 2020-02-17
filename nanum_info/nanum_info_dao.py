from db import database

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