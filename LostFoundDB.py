from flask import Flask, render_template, request, redirect
from db.db import init_db, insert_item, get_all_items

app = Flask(__name__, template_folder="framework")
init_db()

@app.route('/')
def home():
    items = get_all_items()
    return render_template('index.html', items=items)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    desc = request.form['desc']
    location = request.form['location']
    insert_item(name, desc, location)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)