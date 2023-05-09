# Symantec Data Loss Prevention Incidents extractor

<pre>
 ,-.  .   , .   , ,-.  ,    ;-.  ,--. .   , ,---. ,-.   ,.   ,-. ,---.  ,-.  ,-.  
(   `  \ /  |\ /| |  \ |    |  ) |     \ /    |   |  ) /  \ /      |   /   \ |  ) 
 `-.    Y   | V | |  | |    |-'  |-     X     |   |-<  |--| |      |   |   | |-<  
.   )   |   |   | |  / |    |    |     / \    |   |  \ |  | \      |   \   / |  \ 
 `-'    '   '   ' `-'  `--' '    `--' '   `   '   '  ' '  '  `-'   '    `-'  '  '  By: Newton </pre>

Symple python3 extraction tool to gatter/extract the incidents from your DLP into a .csv file that you can work on.

> Tested versions 16.0 MP1, 16.0, 15.8 all the MPs and 15.7

## Requirements

Python 3 installed</br>
cx_Oracle module installed (pip install cx_Oracle)</br>
Connectivity to the Oracle database</br>
Visual C++ 14.0 or greater</br>

## Changes:
> Version 1.2:</br>
> * Now the incident severity shows the real value as HIGH, MEDIUM or LOW</br>
> * Now the incident extraction extracts from the newest incident to the oldest</br>
> * Now it's possible to filter by the incident type using the argument -T or --type</br>

## Arguments:
-r : Define the max number of rows that will be extracted into the final .CSV file (Default it's 30000) </br>
-T : Incident type, you can use this parameter to filter by incident type in the Symantec Data Loss Preventions incidents, if you only want to export a certain type of incidents. The types are, ENDPOINT, NETWORK or DISCOVER.


Username : prompt to insert the DLP database username </br>
Password : prompt to insert the DLP database password </br>
DSN : connection parameters for the DLP, if you run a instance were the Oracle DB it's inside the enforce, should be localhost:1521/protect (if you changed the DLP database name, insert the used name in the after the /) </br>


## .CSV

The .CSV is created in the same folder that you run the script.

The data that will be present in this file will be:
<pre>
INCIDENTID	MESSAGEID	POLICYID	POLICYVERSION	INCIDENTSTATUSID	VIOLATIONCOUNT	DETECTIONDATE	POLICYGROUPID	CUSTOMATTRIBUTESRECORDID	ISDELETED	BLOCKEDSTATUS	INCIDENTSEVERITYID	MESSAGETYPE	DISCOVERITEMID	DISCOVERMILLISSINCEFIRSTSEEN	CREATIONDATE	DATAOWNERID	DATAOWNEREMAILID	ISBLOCKEDSTATUSSUPERSEDED	SHOULDHIDEFROMREPORTS	SHOULDOVERRIDEHIDEFROMREPORTS	MESSAGESOURCE	MESSAGEDATE	DISCOVERVIOLATIONID	POLICYID	POLICY_NAME	DESCRIPTION	DATAOWNER_NAME</pre>

Thanks!



