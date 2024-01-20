import mysql.connector
import json

my_db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="OpenAuto1",
    database="CUSTOMERS"
)


def find_last_entry_id(self):
    conn = my_db.cursor()
    with open('../customers/cid.json', 'r') as outfile:
        customer_id = json.load(outfile)
    return customer_id


