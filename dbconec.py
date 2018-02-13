# postgres
import csv
import psycopg2
conn = psycopg2.connect("dbname='datadb' user=data host='localhost' password='123'")
cur = conn.cursor()
with open('/home/bhavani/Desktop/zipcode.csv','r')as csvfile:
    readfile = csv.reader(csvfile)
    for rows in readfile:

        cur.execute("INSERT INTO demo4 VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],rows[6],rows[7],rows[8],rows[9],rows[10],rows[11],rows[12],rows[13],rows[14],rows[15]))
        conn.commit()
        cur.execute("SELECT * FROM demo4;")
rows = cur.fetchall()
print rows
