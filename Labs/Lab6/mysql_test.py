import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="alex",
    passwd="123",
    db="first_db",
    charset="utf8"
)

cursor = db.cursor()
cursor.execute("INSERT INTO books (name, description) VALUES (%s, %s);", ('Книга', 'Описание книги'))

db.commit()

cursor.execute("SELECT * FROM Books")

books = cursor.fetchall()

print(books)

for book in books:
    print(book)

cursor.close()
db.close()