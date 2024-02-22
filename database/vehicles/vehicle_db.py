import mysql.connector


def row_count(self):
    my_db = mysql.connector.connect(

        host="localhost",
        user="root",
        passwd="OpenAuto1",
        database="CUSTOMERS"
    )
    conn = my_db.cursor()
    query = "SELECT COUNT(*) FROM vehicles"
    conn.execute(query)
    result = conn.fetchone()
    vehicle_row_count = result[0]
    my_db.close()
    return vehicle_row_count

