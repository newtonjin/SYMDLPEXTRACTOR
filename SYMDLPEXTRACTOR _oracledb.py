import oracledb
import csv
import argparse

# parser to -r and -T
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rows", type=int, default=30000, help="Max row number (default: 30000)")
parser.add_argument("-T", "--type", choices=["ENDPOINT", "DISCOVER", "NETWORK", "REST"], default=None, help="Incident type, can be filtered by the types, ENDPOINT, DISCOVER, REST and NETWORK (DEFAULT: ALL TYPES)")
args = parser.parse_args()

# input
print('made by Newton | feel free to contribute!')
user = input("Type the database username: ")
password = input("Type the database password: ")
dsn = input("Type the DSN (host:port/databasename [default port is 1521]): ")

# connection
connection = oracledb.connect(user=user, password=password, dsn=dsn)

# Cursor for the SQL Commands
cursor = connection.cursor()

# Query
query = f"""
SELECT
    INCIDENTATTRIBUTES.INCIDENTID AS ID,
    INCIDENTATTRIBUTES.MESSAGESOURCE AS IncidentSource,
    CASE INCIDENTATTRIBUTES.SEVERITYID
        WHEN 1 THEN 'High'
        WHEN 2 THEN 'Medium'
        WHEN 3 THEN 'Low'
    END AS "Incident Severity",
    INCIDENTATTRIBUTES.CREATIONDATE AS "Occurred On",
    INCIDENTATTRIBUTES.POLICYNAME AS Policy,
    INCIDENTATTRIBUTES.MATCHCOUNT AS Matches,
    INCIDENTATTRIBUTES.INCIDENTSTATUSNAME AS Status,
    RESTMESSAGEINFO.NETWORKPROTOCOL AS NetworkProtocol,
    MESSAGERECIPIENT.RECIPIENTIDENTIFIER AS Destination,
    CASE 
        WHEN INCIDENTATTRIBUTES.MESSAGESOURCE = 'REST' THEN RESTMESSAGEINFO.HTTPURL
        WHEN MESSAGERECIPIENT.URL IS NOT NULL THEN MESSAGERECIPIENT.URL
        ELSE MESSAGERECIPIENT.DOMAIN
    END AS "Destination Path",
    CASE 
        WHEN INCIDENTATTRIBUTES.MESSAGESOURCE = 'DISCOVER' THEN INCIDENTATTRIBUTES.DISCOVERURL
        WHEN MESSAGE.MESSAGESOURCE = 'ENDPOINT' THEN INCIDENTATTRIBUTES.ENDPOINTFILENAME
        WHEN INCIDENTATTRIBUTES.MESSAGESOURCE = 'REST' THEN RESTMESSAGEINFO.COMMONDOCTYPE
    END AS "Source File",
    CASE
        WHEN MESSAGE.MESSAGESOURCE = 'DISCOVER' THEN INCIDENTATTRIBUTES.DISCOVERNAME
        ELSE MESSAGECOMPONENT.NAME
    END AS "Source File Path",
    MESSAGEORIGINATOR.ENDPOINTMACHINENAME AS Machine,
    MESSAGEORIGINATOR.MESSAGEORIGINATORID AS "Device Instance ID",
    CASE
        WHEN INCIDENTATTRIBUTES.MESSAGESOURCE = 'REST' THEN RESTMESSAGEINFO.COMMONAPPLICATIONREPORTNAME
        ELSE INCIDENTATTRIBUTES.ENDPOINTAPPLICATIONNAME
    END AS Application,
    INCIDENTATTRIBUTES.ENDPOINTAPPWINDOWTITLE AS EndpointApptitle,
    INCIDENTATTRIBUTES.INCIDENTSTATUSID AS "Prevention Status",
    INCIDENTATTRIBUTES.MESSAGESUBJECT AS Subject,
    INCIDENTATTRIBUTES.HASATTACHMENT AS "Has Attachment",
    INCIDENTATTRIBUTES.FILEOWNER AS "Data Owner Name",
    INCIDENTATTRIBUTES.FILEOWNEREMAIL AS "Data Owner Email",
    INCIDENTATTRIBUTES.FILEMODIFIEDBY AS "User",
    CASE
        WHEN INCIDENTATTRIBUTES.MESSAGESOURCE = 'REST' THEN RESTMESSAGEINFO.LOCATIONREGION
    END AS Location,
    INCIDENTATTRIBUTES.ENDPOINTAPPLICATIONPATH AS ApplicationPATH
FROM 
    INCIDENTATTRIBUTES
    LEFT JOIN APPLICATION ON INCIDENTATTRIBUTES.ENDPOINTAPPLICATIONNAME = APPLICATION.PRODUCTALIAS
    LEFT JOIN MESSAGERECIPIENT ON INCIDENTATTRIBUTES.MESSAGEID = MESSAGERECIPIENT.MESSAGEID
    LEFT JOIN MESSAGE ON INCIDENTATTRIBUTES.MESSAGEID = MESSAGE.MESSAGEID
    LEFT JOIN RESTMESSAGEINFO ON INCIDENTATTRIBUTES.MESSAGEID = RESTMESSAGEINFO.MESSAGEID
    LEFT JOIN (
        SELECT MESSAGECOMPONENT.MESSAGEID, MESSAGECOMPONENT.NAME
        FROM MESSAGECOMPONENT
        WHERE MESSAGECOMPONENT.COMPONENTTYPE = 3
    ) MESSAGECOMPONENT ON INCIDENTATTRIBUTES.MESSAGEID = MESSAGECOMPONENT.MESSAGEID
    LEFT JOIN MESSAGEORIGINATOR ON MESSAGE.MESSAGEORIGINATORID = MESSAGEORIGINATOR.MESSAGEORIGINATORID
WHERE 
    (INCIDENTATTRIBUTES.MESSAGESOURCE = :type OR :type IS NULL)
ORDER BY 
    INCIDENTATTRIBUTES.INCIDENTID DESC
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
