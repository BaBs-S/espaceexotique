from flask import Flask, render_template, request, redirect, send_from_directory
from flask_mysqldb import MySQL
import sqlite3 
import os



app = Flask(__name__)
# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "root"
# app.config["MYSQL_DB"] = "espaceexotique"
# mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')




# @app.route('/produits', methods=['POST', 'GET'])
# def products():
#     return render_template('produits.html')

# @app.route('/contacts', methods=['POST', 'GET'])
# def contact():
#     return render_template('contact.html')


# @app.route('/catalogue')
# def download():
#     return send_from_directory(directory='static', path='pdf/catalogue.pdf', as_attachment=True)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
    #app.run(host='10.11.96.151', port=5000, debug=True)