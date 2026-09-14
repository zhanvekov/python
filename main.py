import requests
from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import sqlite3
import random

app = Flask(__name__)
app.secret_key = "admin_key"

class HomeWork:
    def __init__(self, head, body, group, url):
        self.head = head
        self.body = body
        self.group = group
        self.url = url
    
    def info(self):
        print(f'Заголовок: {self.head}')
        print(f'Тело: {self.body}')
        print(f'Группа: {self.group}')
        print(f'Ссылка: {self.url}')

homework1 = HomeWork(
    head="Создать класс в Python",
    body="Создать класс HomeWork с атрибутами head, body, group и url.",
    group="1",
    url="https://example.com/python-homework"
)

homework2 = HomeWork(
    head="Изучить FastAPI",
    body="Создать простой GET и POST роут для получения домашних заданий.",
    group="2",
    url="https://example.com/fastapi"
)

homework3 = HomeWork(
    head="Решить задачи по математике",
    body="Решить задачи №1-10 из практической работы.",
    group="3",
    url="https://example.com/math"
)

api_key = ["123", '321']

@app.route('/api/get_homework', methods=['POST', 'GET'])
def homework_page():
    if request.method == 'GET':
        return render_template('get_homework.html')
    
    group = request.form['group']
    key = request.form['key']

    if key not in api_key:
        return "error", 401
    
    else:

        if group == '1':
            js = {
                "head": homework1.head,
                "body": homework1.body,
                "group": homework1.group,
                "url": homework1.url
            }

            return jsonify(js)
        
        elif group == '2':
            js = {
                "head": homework2.head,
                "body": homework2.body,
                "group": homework2.group,
                "url": homework2.url
            }

            return jsonify(js)

        elif group == '3':
            js = {
                "head": homework3.head,
                "body": homework3.body,
                "group": homework3.group,
                "url": homework3.url
            }

            return jsonify(js)

        else:
            return "error", 401



@app.route('/html')
def html_page():
    return '''
    <h1>Hello</h1>
    <img src="data:image/jpeg;base64,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" alt="картина">
    '''




# @app.route('/login', methods=['POST', 'GET'])
# def login_page():
#     error = False

#     if request.method == 'POST':
#         login = request.form['login']
#         password = request.form['password']

#         conn = sqlite3.connect('my_database.db')
#         cursor = conn.cursor()

#         cursor.execute("select login, password from Users where login=?", (login,))
#         user = cursor.fetchone()
#         conn.commit()
#         conn.close()

#         if (user and user[1] == password):
#             session['username'] = login
#             session['password'] = password
#             return render_template('file2.html', login=login)
        
#         error = True

#     return render_template("file.html", error=error)

# @app.route('/main', methods=['POST', 'GET'])
# def main_page():
#     login = session.get('username')
#     return render_template('file2.html', login=login)

# @app.route('/change_password', methods=['POST', 'GET'])
# def password_page():
#     error = False
#     if request.method == 'POST':
#         old_password = request.form['old_password']
#         new_password = request.form['new_password']
#         login = session.get('username')
#         conn = sqlite3.connect('my_database.db')
#         cursor = conn.cursor()

#         cursor.execute("select login, password from Users where login=? and password=?", (login, old_password,))
#         user = cursor.fetchone()
    

#         if user:
#             cursor.execute('update Users set password=? where login=?', (new_password, user[0]))
#             conn.commit()
#             conn.close()

#             return render_template('file2.html', login=login)

#         conn.close()
        
#         error = True
        
#     return render_template('file3.html', error=error)

# @app.route('/homework', methods=['GET'])
# def homework_page():
#     if request.method == 'GET':
#         username = session.get('username')

#         conn = sqlite3.connect('my_database.db')
#         cursor = conn.cursor()
#         cursor.execute('select title, description, avatar from Homework where login=?', (username,))
#         ls = cursor.fetchall()
#         conn.commit()
#         conn.close()

#         return render_template('homework.html', ls=ls)
    

# @app.route('/add_homework', methods=['POST', 'GET'])
# def add_homework_page():
#     error = False
#     if request.method == 'GET':
#         return render_template('create_homework.html')
#     else:
#         username = session.get('username')
#         title = request.form['title']
#         description = request.form['description']
#         avatar = request.files['avatar']

#         if title and description and avatar.filename:
#             avatar.save('static/uploads/' + avatar.filename)
#             avatar_path = 'uploads/' + avatar.filename

#             conn = sqlite3.connect('my_database.db')
#             cursor = conn.cursor()

#             cursor.execute('insert into Homework(title, description, avatar, login) values(?, ?, ?, ?)', (title, description, avatar_path, username))
#             cursor.execute('select title, description, avatar from Homework where login=?', (username,))
#             ls = cursor.fetchall()
#             conn.commit()
#             conn.close()

#             return render_template('homework.html', ls=ls)

#         else:

#             error = True
#             return render_template('create_homework.html', error=error)

    




app.run(host="0.0.0.0", port=3000)
