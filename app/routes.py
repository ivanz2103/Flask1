from app import app 
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/favoriteFive')
def favoriteFive():
    fun = ['Elden Ring', 'Ratchet and Clank', 'NFSU2', 'COC', 'Skate']

    return render_template('favoriteFive.html', games=fun)
