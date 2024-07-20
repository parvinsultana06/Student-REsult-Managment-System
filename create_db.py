import sqlite3
def create_db():
    con=sqlite3.connect(database="Result Project.db")
    #con=sqlite3.connect(database="Login_with_database.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text, duration text, charges text, description text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,addmission text,course text,state text,city text,address text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,contact text,email text,question text,answertext,passwordtext)")
    con.commit()
    
    
    con.close()
    
create_db()