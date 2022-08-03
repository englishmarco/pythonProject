import pymysql

print('连接到mysql服务器...')
db = pymysql.connect(
        host="localhost",
        user="root",
        passwd="root",
        port = 3306,
        db="guest",
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
print('连接上了!')
cursor = db.cursor()


insert_color = ("INSERT INTO twocolorball(id,date,period,first,second,third,fourth,fifth,sixth,basketball)" "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
dese = (id,date,period,first,second,third,fourth,fifth,sixth,basketball)
cursor.execute(insert_color, dese)
db.commit()