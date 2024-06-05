from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__, static_url_path='/static')


def get_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM data")
    rows = c.fetchall()
    conn.close()
    return rows

# Define a route for the root URL ('/')
@app.route('/')
def index():
    from scraper import check_aurora
    if check_aurora():
        return 'Aurora is happening nearby!'
    else:
        return 'No aurora forecast nearby.'

if __name__ == '__main__':
    app.run(debug=True)

