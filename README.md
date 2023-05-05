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


## Arguments:
-r : Define the max number of rows that will be extracted into the final .CSV file (Default it's 30000) </br>
Username : prompt to insert the DLP database username </br>
Password : prompt to insert the DLP database password </br>
DSN : connection parameters for the DLP, if you run a instance were the Oracle DB it's inside the enforce, should be localhost:1521/protect (if you changed the DLP database name, insert the used name in the after the /) </br>


## .CSV

the .CSV is created in the same folder that you run the script.

Thanks!



