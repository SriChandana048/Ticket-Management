from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import mysql.connector

app=Flask(__name__)

db_config = {
    'host': 'localhost',
    'user' : 'root',
    'password' : 'PC1430',
    'database' : 'ticket'
}

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/tickets',methods=['GET'])
def tickets():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    query=''' SELECT ticket_id, title, ticket_description,creation_date, last_updated, category, ticket_status FROM tickets'''
    cursor.execute(query)
    tickets=cursor.fetchall()
    print(tickets)
    conn.close()
    cursor.close()
    return render_template("tickets.html",tickets=tickets)

@app.route('/submit',methods=['POST'])
def submit():
    title=request.form.get('title')
    desc=request.form.get('description')
    created_date=request.form.get('creation_date')
    updated=request.form.get('last_updated')
    category=request.form.get('category')
    status=request.form.get('status')

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = """ INSERT INTO tickets (title, ticket_description, creation_date, last_updated, category, ticket_status)
            VALUES (%s, %s, %s, %s, %s, %s) """
    data = (title, desc, created_date, updated, category, status)
    conn.commit()
    message = f"Ticket '{title}' has been submitted successfully!"
    return message



if __name__=="__main__":
    app.run(debug='false')
