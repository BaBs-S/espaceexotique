from flask import Flask, render_template, request, redirect, send_from_directory
from flask_mysqldb import MySQL
import sqlite3 
import os



app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')





if __name__ == "__main__":
    app.run()
    
