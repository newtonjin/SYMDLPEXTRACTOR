import cx_Oracle
import csv
import argparse

# parser to -r
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rows", type=int, default=30000, help="Max row number (default: 30000)")
args = parser.parse_args()

# input
user = input("Type the database username: ")
password = input("Type the database password: ")
dsn = input("Type the DSN (Usually it's in the format host:port/databasename [default port is 1521]): ")

# connection
connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)

# Cursor for the SQL Commands
cursor = connection.cursor()

# Query
query = f"""
SELECT i.*, p.POLICYID, p.NAME AS POLICY_NAME, p.DESCRIPTION, do.NAME AS DATAOWNER_NAME
FROM INCIDENT i
JOIN POLICY p ON i.POLICYID = p.POLICYID
LEFT JOIN DATAOWNER do ON i.DATAOWNERID = do.DATAOWNERID
FETCH FIRST {args.rows} ROWS ONLY
"""
cursor.execute(query)

# CSV file
with open("incident.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow([i[0] for i in cursor.description])  # first row
    for row in cursor:
        writer.writerow(row)

#close con
cursor.close()
connection.close()
