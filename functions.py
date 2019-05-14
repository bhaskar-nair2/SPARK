import pymysql as sql
import os
# try:
# with conn.cursor() as cur:
#        cur.execute("Select * from sites")
# res,rep=cur.fetchone()
# print(res,rep)
# finally:
# conn.close()


def search(typ, val):
    que = "SELECT DNS FROM SITES WHERE WORD LIKE %s"
    conn = sql.connect("localhost", "root", "toor", "proj")
    try:
        with conn.cursor() as cur:
            cur.execute(que, (typ))
            fin = str(cur.fetchone())
            nin = fin.split('\'')[1]
            nin = nin+val
            os.startfile(nin)
    finally:
        conn.close()
