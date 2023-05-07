import cx_Oracle
import csv
import argparse

# parser to -r and -T
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rows", type=int, default=30000, help="Max row number (default: 30000)")
parser.add_argument("-T", "--type", choices=["ENDPOINT", "DISCOVER", "NETWORK"], default=None, help="Incident type, can be filtered by the types, ENDPOINT, DISCOVER and NETWORK (DEFAULT: ALL TYPES)")
args = parser.parse_args()

# input
print('made by Newton | feel free to contribute!')
user = input("Type the database username: ")
password = input("Type the database password: ")
dsn = input("Type the DSN (host:port/databasename [default port is 1521]): ")

# connection
connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)

# Cursor for the SQL Commands
cursor = connection.cursor()

# Query
query = f"""
SELECT i.*, 
  CASE i.INCIDENTSEVERITYID 
    WHEN 1 THEN 'High' 
    WHEN 2 THEN 'Medium' 
    WHEN 3 THEN 'Low' 
    ELSE '' 
  END AS INCIDENTSEVERITY, 
  p.POLICYID, p.NAME AS POLICY_NAME, p.DESCRIPTION, do.NAME AS DATAOWNER_NAME
FROM INCIDENT i
JOIN POLICY p ON i.POLICYID = p.POLICYID
LEFT JOIN DATAOWNER do ON i.DATAOWNERID = do.DATAOWNERID
WHERE (i.MESSAGESOURCE = :type OR :type IS NULL)
ORDER BY i.INCIDENTID DESC
FETCH FIRST {args.rows} ROWS ONLY
"""

# cursor
cursor.execute(query, type=args.type)

# CSV file
with open("incident.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow([i[0] for i in cursor.description])  # first row
    for row in cursor:
        writer.writerow(row)

#close con
cursor.close()
connection.close()
