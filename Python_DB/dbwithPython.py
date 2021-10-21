import sqlite3
## To connect to the database
conn = sqlite3.connect('test.db')

with conn:
    ## Used to execute SQL commands with Python
    cur = conn.cursor()
    ## Creates a table if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_things(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_things TEXT \
        )")
    ## Makes sure the changes are made in the database
    conn.commit()
## Closes the connection to the database    
conn.close()

## File list with various documents
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

## Filters out files ending with .txt
txtFiles =list(filter(lambda x: x[-4:] == '.txt', fileList))

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    ## Loops through the txt file and insert value into the tbl
    for i in txtFiles:
        cur.execute("INSERT INTO tbl_things(col_things) VALUES (?)", \
                (i,))
        conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    ## Select the table and the values
    cur.execute("SELECT ID, col_things FROM tbl_things")
    selectAll = cur.fetchall()
    ## Will print out all data that has been selected
    for item in selectAll:
        msg = "Text files: {}".format(item,)
        print(msg)
conn.close()

