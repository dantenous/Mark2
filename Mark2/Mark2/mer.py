import sqlite3
from sqlite3 import Error
import smbus2
import bme280


port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn


database = r"/home/pi/db/db.sqlite3"
conn = create_connection(database)
cur = conn.cursor() 

cur.execute("INSERT INTO domacnost(cas,teplota,tlak,vlhkost) VALUES('"+data.timestamp+"', '"+data.temperature+"', '"+data.pressure+"', '"+data.humidity+"'")
conn.commit()
cur.close()


print(data.timestamp)
print(data.temperature)
print(data.pressure)
print(data.humidity)

