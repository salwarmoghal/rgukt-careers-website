import mysql.connector
credentials={
"mysql_host" : 'localhost',
"mysql_user" : 'root',
"mysql_password" : 'Sulthan7866129@',
"mysql_db" : 'rgukt',
}
def loadDB() :

    # credentials = {}

    cnx = mysql.connector.connect(user = credentials['mysql_user'], password = credentials['mysql_password'], host = credentials['mysql_host'], database = credentials['mysql_db'])
    cur = cnx.cursor(dictionary=True)
    return cnx,cur

