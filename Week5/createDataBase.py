from faker import Faker
import psycopg2

con = psycopg2.connect(database="persons",
                       user="postgres", password="8951",
                       host="localhost", port="5432")
print("Database persons is opened")
cur = con.cursor()
cur.execute('''CREATE TABLE PERSON (ID INT NOT NULL,
                                      Name TEXT NOT NULL,
                                      Address TEXT NOT NULL,
                                      age INT NOT NULL,
                                      review TEXT);''')
print("Table PERSON was created successfully")
fake = Faker()
for i in range(100000):
    print("#"+str(i))
    cur.execute("INSERT INTO PERSON (ID,Name,Address, age, review) VALUES ('" +
                str(i) + "','" + fake.name() + "','" +
                fake.address() + "','" + str(fake.random_int(1, 120)) +
                "','" + fake.text() + "')")
    con.commit()
print("Finished")


