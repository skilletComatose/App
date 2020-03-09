#from __init__ import app

from flask_mysqldb import MySQL
import redis
#import redis
#import json
#
#app.config['MYSQL_HOST'] = 'SQL'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'nobody'
#app.config['MYSQL_DB'] = 'mysql'
#mysql = MySQL(app)

class ConexionSQL:
    def __init__(self,cur,js,mys):
        self.cursor = cur
        self.Json = js
        self.mysql = mys

    def Create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tabla1 ( info JSON NOT NULL )")
    
    def Insert_data(self):
        self.cursor.execute("INSERT INTO tabla1  VALUES (%s)",(self.Json,) )
        self.mysql.connection.commit()
        self.cursor.close()

class ConexionRedis:
    def __init__(self,ho,jfi):
        self.host = ho
        self.jsonfile = jfi
    
    def Insert_data(self):
        r_server = redis.Redis(self.host)
        r_server.set("info",self.jsonfile)
        
    #cur->cursor = mysql.connection.cursor()
    #query = "CREATE TABLE IF NOT EXISTS tabla1 ( info JSON NOT NULL )"  
    #cursor.execute(query)


    #cursor.execute("INSERT INTO tabla1  VALUES (%s)", (jsonfile,))
    #mysql.connection.commit()
    #cursor.close()

    #r_server = redis.Redis("redis")
    #r_server.set("info",jsonfile)    

