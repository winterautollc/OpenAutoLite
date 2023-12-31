import mysql.connector

my_db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="OpenAuto1",
    database="CUSTOMERS"
)


def find_last_entry_id(self):
    conn = my_db.cursor()
    key_id = "SELECT LAST_INSERT_ID(customer_id) FROM customers"
    conn.execute(key_id)
    for row in conn:
        last_id = row[0]
        return last_id
