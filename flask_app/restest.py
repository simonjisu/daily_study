from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'irisuser'
app.config['MYSQL_DATABASE_PASSWORD'] = 'irisuser'
app.config['MYSQL_DATABASE_DB'] = 'baseball'
app.config['MYSQL_DATABASE_HOST'] = '210.183.11.122'
mysql.init_app(app)

@app.route('/')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''SELECT personid, SUM(bat1b) AS sum1b FROM test GROUP BY personid''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})

if __name__ == '__main__':
    app.run()

