# SYMDLPEXTRACTOR (Symantec Data Loss Prevention Extractor) PY 3

 (       )   *    (     (    (          )        (                            )  (     
 )\ ) ( /( (  `   )\ )  )\ ) )\ )    ( /(   *   ))\ )   (       (    *   ) ( /(  )\ )  
(()/( )\()))\))( (()/( (()/((()/((   )\())` )  /(()/(   )\      )\ ` )  /( )\())(()/(  
 /(_)|(_)\((_)()\ /(_)) /(_))/(_))\ ((_)\  ( )(_))(_)|(((_)(  (((_) ( )(_)|(_)\  /(_)) 
(_))__ ((_|_()((_|_))_ (_)) (_))((_)__((_)(_(_()|_))  )\ _ )\ )\___(_(_())  ((_)(_))   
/ __\ \ / /  \/  ||   \| |  | _ \ __\ \/ /|_   _| _ \ (_)_\(_|(/ __|_   _| / _ \| _ \  
\__ \\ V /| |\/| || |) | |__|  _/ _| >  <   | | |   /  / _ \  | (__  | |  | (_) |   /  
|___/ |_| |_|  |_||___/|____|_| |___/_/\_\  |_| |_|_\ /_/ \_\  \___| |_|   \___/|_|_\  
By: Newton

Symple python3 extraction tool to gatter raw data from the incidents into a .csv file that you can work on.

Arguments:
-r : Define the max number of rows that will be extracted into the final .CSV file
Username : prompt to insert the DLP database username
Password : prompt to insert the DLP database password
DSN : connection parameters for the DLP, if you run a instance were the Oracle DB it's inside the enforce, should be localhost:1521/protect (if you changed the DLP database name, insert the used name in the after the /)

the .CSV is created in the same folder that you run the script.

Thanks!



