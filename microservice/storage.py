from flask_mysqldb import MySQL
import redis
import json

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
        r_server.incr("index", 1) 
        index = r_server.get("index").decode("utf-8")
        key = int(index)
        new_d = json.loads(self.jsonfile)
        r_server.hmset(key,new_d)

   