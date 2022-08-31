from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    msg = 'Hello World'
    return render_template('home.html', msg=msg)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')