from flask import Flask,render_template,request
from flask_mysqldb import MySQL
#import redis
from microservice.adapter2 import Convertir
from microservice.storage import ConexionRedis, ConexionSQL
import json




def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config['MYSQL_HOST'] = 'SQL'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'nobody'
    app.config['MYSQL_DB'] = 'mysql'
    mysql = MySQL(app)
    
    @app.route("/index")
    def index():
        return render_template("index.html")

    @app.route('/', methods=['POST', 'GET'])
    def guardar():
         
        if(request.method == 'POST'):
            temperatura = request.form['temp']
            tiempo = request.form['tiempo']
            
            if( temperatura and tiempo):
                Datosbase = Convertir( temperatura , tiempo )  #un objeto del tipo adaptador (patron adaptado y estrategia)               
                
                Json = Datosbase.htmlToJson() #aquí se ejecita el patron adaptador 

                conecSQL = ConexionSQL( mysql.connection.cursor(), Json  ,mysql ) #un obejeto del tipo conexion para manipular sql
                conecSQL.Create_table()
                conecSQL.Insert_data()

                conecRedis = ConexionRedis("redis",Json)
                conecRedis.Insert_data()

        return render_template("form.html")
          
    @app.route("/iot", methods=['GET', 'POST'])
    def iot():
        ata = request.get_json()
        if(request.method=='POST' and ata):
            data = json.dumps(ata)

            conecSQL = ConexionSQL( mysql.connection.cursor(), data  ,mysql ) #un obejeto del tipo$
            conecSQL.Create_table()
            conecSQL.Insert_data()

            conecRedis = ConexionRedis("redis",data)
            conecRedis.Insert_data()
            return data    
    
    return app

