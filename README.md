# Symantec Data Loss Prevention Incidents extractor

<pre>
 ,-.  .   , .   , ,-.  ,    ;-.  ,--. .   , ,---. ,-.   ,.   ,-. ,---.  ,-.  ,-.  
(   `  \ /  |\ /| |  \ |    |  ) |     \ /    |   |  ) /  \ /      |   /   \ |  ) 
 `-.    Y   | V | |  | |    |-'  |-     X     |   |-<  |--| |      |   |   | |-<  
.   )   |   |   | |  / |    |    |     / \    |   |  \ |  | \      |   \   / |  \ 
 `-'    '   '   ' `-'  `--' '    `--' '   `   '   '  ' '  '  `-'   '    `-'  '  '  By: Newton </pre>

Symple python3 extraction tool to gatter raw data from the incidents into a .csv file that you can work on.

## Arguments:
-r : Define the max number of rows that will be extracted into the final .CSV file </br>
Username : prompt to insert the DLP database username </br>
Password : prompt to insert the DLP database password </br>
DSN : connection parameters for the DLP, if you run a instance were the Oracle DB it's inside the enforce, should be localhost:1521/protect (if you changed the DLP database name, insert the used name in the after the /) </br>


## .CSV

the .CSV is created in the same folder that you run the script.

Thanks!



