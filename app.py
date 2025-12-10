import os
from flask import Flask
import pymysql
pymysql.install_as_MySQLdb()

from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL()

mysql_database_host = os.environ.get("MYSQL_DATABASE_HOST", "localhost")

# MySQL configurations
app.config['MYSQL_USER'] = 'db_user'
app.config['MYSQL_PASSWORD'] = 'Passw0rd'
app.config['MYSQL_DB'] = 'employee_db'
app.config['MYSQL_HOST'] = mysql_database_host

mysql.init_app(app)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/how are you")
def hello():
    return "I am good, how about you?"

@app.route("/read from database")
def read():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    return ",".join(str(r[0]) for r in rows)

if __name__ == "__main__":
    app.run()
