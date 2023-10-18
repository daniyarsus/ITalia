import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )

    print("db is runned")

except Exception as ex:
    print("error")
    print(ex)

