import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_things(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_things TEXT \
        )")
    conn.commit()
conn.close()

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

txtFiles =list(filter(lambda x: x[-4:] == '.txt', fileList))

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    for i in txtFiles:
        cur.execute("INSERT INTO tbl_things(col_things) VALUES (?)", \
                (i,))
        conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT ID, col_things FROM tbl_things")
    selectAll = cur.fetchall()
    for item in selectAll:
        msg = "Text files: {}".format(item,)
        print(msg)
conn.close()

