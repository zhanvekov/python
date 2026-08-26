import requests
from flask import Flask, request, render_template
import sqlite3


conn = sqlite3.connect('my_database.db')
app = Flask(__name__)
cursor = conn.cursor()


@app.route('/html')
def html_page():
    return '''
    <h1>Hello</h1>
    <img src="data:image/jpeg;base64,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" alt="картина">
    '''

@app.route('/create_user', methods=['POST'])
def create_page():
    data = request.json
    login = data['login']
    password = data['password']

    cursor.execute("select login from Users where login=?", (login,))
    user = cursor.fetchone()
    if user:
        return "такой пользователь уже существует."
    elif len(password) < 8:
        return "в пароле меньше 8 символов"
    elif password[0].islower():
        return "первая буква пароля не заглавная"
    else:
        cursor.execute("insert into Users(login, password) values(?, ?)", (login, password,))
        return "успешно!"

@app.route('/auth_user', methods=['POST'])
def authorization_page():
    data = request.json
    login = data['login']
    password = data['password']

    cursor.execute("select login from Users where login=?", (login,))
    login_user = cursor.fetchone()
    cursor.execute("select password from Users where login=?", (login,))
    password_user = cursor.fetchone()
    cursor.execute("select quantity from Users where login=?", (login,))
    quantity_user = cursor.fetchone()



    if login_user == None:
        return "нет такого пользователя."
    
    elif quantity_user[0] >= 5:
        return "вход заблокирован."
    
    elif password != password_user[0]:
        cursor.execute("update Users set quantity = quantity + 1 where login=?", (login,))
        conn.commit()
        return "неверный пароль повторите еще раз."
    
    else:
        return "успешно!"

@app.route('/Word', methods=['POST'])
def word_page():
    secret_word = "python"
    data = request.json
    word = data['word']

    if secret_word != word:
        return "неугадали"
    else:
        return "угадали"

conn.commit()
app.run()
conn.close()