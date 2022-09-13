import mysql.connector
from mysql.connector import Error
from datetime import datetime


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', database="asset_manager", user='root', password='')
        if conn.is_connected():
            dt = datetime.now()
            print('Connected to MySQL database')
            my_cursor = conn.cursor()
            my_cursor.execute(f"INSERT INTO `tbl_active_asset`(asset_id,date_time) VALUES ('3','{dt}')")
            conn.commit()
            for i in my_cursor:
                print(i)

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()