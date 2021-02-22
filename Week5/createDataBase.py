from faker import Faker
import psycopg2

con = psycopg2.connect(database="customers", user="postgres", password="8951", host="localhost", port="5432")
print("Database is opened")
cur = con.cursor()
cur.execute('''CREATE TABLE CUSTOMER (ID INT PRIMARY KEY NOT NULL,
                                      Name TEXT NOT NULL,
                                      Address TEXT NOT NULL,
                                      review TEXT);''')
print("Table is created successfully")
fake = Faker()
for i in range(100000):
    print("#"+str(i))
    cur.execute("INSERT INTO CUSTOMER (ID,Name,Address,review) VALUES ('" +
                str(i) + "','" + fake.name() + "','" +
                fake.address() + "','" + fake.text() + "')")
    con.commit()
print("Finished")