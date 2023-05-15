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
Connectivity to the Oracle database</br>
IF YOUR PYTHON IS IN VERSION 3.10 or GREATER:
oracledb module installed (pip install oracledb)</br>

IF YOUR PYTHON IS IN VERSION 3.9 OR ABOVE:
cx_Oracle module installed (pip install cx_Oracle)</br>
Visual C++ 14.0 or greater</br>

## Attention
If you are using python 3.9 or lower use the standart version, if you are using python 3.10 or greater use the _oracle version!


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
ID	INCIDENTSOURCE	Incident Severity	Occurred On	POLICY	MATCHES	STATUS	DESTINATION	Destination Path	Source File	Source File Path	MACHINE	Device Instance ID	ENDPOINTAPPTITLE	Prevention Status	SUBJECT	Has Attachment	Data Owner Name	Data Owner Email	User	APPLICATION	APPLICATIONPATH
</pre>



## Changes:
> Version 2.0</br>
> * Changed the informations extracted in the database to match similarly to the report in the DLP enforce</br>
> * Changed the query to look up more valid information</br>
> * Inserted a new .py file in the github for the python 3.10 and greater, because cx_Oracle wasn't updated</br>


> Version 1.2:</br>
> * Now the incident severity shows the real value as HIGH, MEDIUM or LOW</br>
> * Now the incident extraction extracts from the newest incident to the oldest</br>
> * Now it's possible to filter by the incident type using the argument -T or --type</br>

Thanks!



