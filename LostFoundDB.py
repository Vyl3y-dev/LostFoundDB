from flask import Flask, render_template, request, redirect
from db.db import init_db, insert_item, get_all_items

app = Flask(__name__, template_folder="framework")
init_db()

@app.route('/')
def home():
    items = get_all_items()
    return render_template('index.html', items=items)

@app.route("/add")
def show_form():
    return render_template("form.html")
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    desc = request.form['desc']
    location = request.form['location']
    foundBy = request.form['foundBy']
    claimed = request.form['claimed']
    claimedBy = request.form['claimedBy']
    loggedBy = request.form['loggedBy']
    dateAdded = request.form['dateAdded']
    dateClaimed = request.form['dateClaimed']
    insert_item(name, desc, location, foundBy, claimed, claimedBy, loggedBy, dateAdded, dateClaimed)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)