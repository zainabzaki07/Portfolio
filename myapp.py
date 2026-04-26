from flask import Flask, request
app = Flask(__name__)
from flask import render_template,url_for,redirect, flash
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'portfolio.db')
#for flash use only...
app.secret_key = 'my_very_secret_key'
def get_db_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
def query_db(query, args=(), one=False):
    cur = get_db_connection().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
def to_camel_case(text):
    # Split by common separators (space or underscore)
    words = text.replace('_', ' ').split()
    if not words:
        return ""
    print(words)
    # Keep the first word lowercase and capitalize the rest
    return ' '.join(word.capitalize() for word in words[:])

    
@app.route('/Courses')
def Courses():
    return render_template("Courses.html")

@app.route('/', methods=['GET', 'POST'])
def index():
    image_src = "/static/me-priv.png"
    users={}
    msg=""
    if request.method=="GET":
        for user in query_db('select * from reviews'):
            users[user[0]]=user
        files={"myimage":image_src,"data":users,"recordcount":len(users.keys())}
        return render_template("myhtml.html",values=files)
    else:
        name = request.form['name']
        name=to_camel_case(name)
        level = request.form['level']
        subject = request.form['subject']
        rating = request.form['rating']
        comments = request.form['comments']
        if rating==None or rating=="":
            msg="Please give some rating too."
            type="danger"
            flash(msg,type)
        else:
            type="success"
            conn=get_db_connection()
            conn.execute(
            'INSERT INTO reviews (name,subject,level,rating,comments) VALUES ( ?,? ,? ,? ,?)',
            (name, subject,level,rating,comments)
            )
            conn.commit()
            conn.close()
            msg="Testimonial Successfully submitted!"
            flash(msg,type)
        return redirect(url_for("index"))
       
        

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(host="localhost", port=int("3000"))
