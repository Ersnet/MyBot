import pymysql

def save_data(group_id, message, msg_id, user_id, nickname, time):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", charset="utf8mb4", db="qqbotdata")
    cursor = conn.cursor()

    a, b, c, d, e, f = f'{group_id}', "'" + message + "'", f'{msg_id}', f'{user_id}', "'" + nickname + "'", f'{time}'
    cursor.execute(f"insert into qqtb(group_id, message, msg_id, user_id, nickname, time) values({a}, {b}, {c}, {d}, {e}, {f})")
    conn.commit()

    cursor.close()
    conn.close()

def get_data(time, user_id):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", charset="utf8mb4", db="qqbotdata")
    cursor = conn.cursor()

    cursor.execute(f"select * from qqtb where time > {time} and time < {time + 15} and user_id = {str(user_id)}")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data[0][1]

def get_data_test(time, user_id):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", charset="utf8mb4", db="qqbotdata")
    cursor = conn.cursor()

    cursor.execute(f"select * from qqtb where time > {time} and time < {time + 15} and user_id = {str(user_id)}")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data