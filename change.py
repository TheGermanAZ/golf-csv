# import csv

# reader = csv.reader(open("dup.csv", "r"), delimiter=',')
# writer = csv.writer(open("output.csv", 'w'), delimiter=';')

# writer.writerows(reader)
from dotenv import load_dotenv
load_dotenv()
import os
import MySQLdb

cnx = MySQLdb.connect(
  host= os.getenv("DB_HOST"),
  user=os.getenv("DB_USERNAME"),
  passwd= os.getenv("DB_PASSWORD"),
  db= os.getenv("DB_NAME"),
  autocommit = True,
  ssl_mode = "VERIFY_IDENTITY",
  ssl      = {
    "ca": "/etc/ssl/certs/ca-certificates.crt"
  }
)
  

import csv

andreport = 'output.csv'


cursor = cnx.cursor()

with open(andreport, mode='r') as csv_data:
    reader = csv.reader(csv_data, delimiter=';')
    csv_data_list = list(reader)
    for row in csv_data_list:
      print(row)
      cursor.execute("""
                   INSERT INTO `golf-catalog_post`(
                   name, price, imageref)
                   VALUES(%s,%s,%s)""",
                    (row[0], row[1], row[2],))
cnx.commit()
cursor.close()
cnx.close()
print("Done")
