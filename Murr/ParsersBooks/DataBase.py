# -*- coding: utf-8 -*-

import mysql.connector
from ParsersBooks.ParserProse import books

connection = mysql.connector.connect(host = 'localhost',
                             user = 'root',
                             password = '89379608523QqQ',
                             database = 'books')

cursor = connection.cursor()
#cursor.execute('SELECT * FROM Books_info ORDER BY Rating DESC')
#cursor.execute('ALTER TABLE Books_info MODIFY Link VARCHAR(150)')
#cursor.execute('CREATE TABLE Books_info(Title VARCHAR(50), PRIMARY KEY(Title), Author VARCHAR(50), Genre VARCHAR(40), Rating VARCHAR(15), Year VARCHAR(15), Size VARCHAR(15),  Description VARCHAR(2048) , Image VARCHAR(100), Link VARCHAR(100))')
for number in range(len(books)):
    cursor.execute('REPLACE INTO Books_info VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', [books[number]['title'], books[number]['author'], books[number]['genre'], books[number]['rating'], books[number]['year'], books[number]['size'], books[number]['description'], books[number]['img'], books[number]['link']])
cursor.execute('commit')
#cursor.execute('ALTER TABLE Books_info(Title VARCHAR(30) NOT NULL PRIMARY KEY(Title), Author VARCHAR(30) NOT NULL, Genre VARCHAR(30) NOT NULL, Rating VARCHAR(15), Year VARCHAR(15), Size VARCHAR(15),  Description VARCHAR(1024) , Image VARCHAR(50), Link VARCHAR(50))')
