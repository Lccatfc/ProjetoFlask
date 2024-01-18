import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="lucca"
)

mycursor = mydb.cursor()

def insere(email, nome, age):
  mycursor.execute(f"INSERT INTO tabelanova (email, name, age) VALUES('{email}', '{nome}', '{age}')")
  mydb.commit()



def myResult(coluna):
  mycursor.execute(f"SELECT {coluna} FROM tabelanova")
  myresult = mycursor.fetchall()
  return myresult
