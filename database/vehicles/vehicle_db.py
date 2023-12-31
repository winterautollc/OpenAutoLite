import mysql.connector

my_db = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="Crapface223",
    database="CUSTOMERS"
)
create_vehcile = """CREATE TABLE vehicles (
                        platenum VARCHAR(255),
                        vin VARCHAR(255),
                        year VARCHAR(255),
                        make VARCHAR(255),
                        model VARCHAR(255),
                        trim VARCHAR(255),
                        engine VARCHAR(255)
                        id INT NOT NULL AUTO_INCREMENT,
                        PRIMARY KEY (id)
);"""

conn = my_db.cursor()
conn.execute(create_vehcile)
my_db.close()