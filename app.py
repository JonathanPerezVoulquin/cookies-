from flask import Flask, render_template, request, make_response

app = Flask(__name__)
app.secret_key = 'my_secret_key'


@app.route('/')
def index():
    return render_template('cookie.html')


@app.route('/cookie', methods=['GET', 'POST'])
def setCookie():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp


@app.route('/getcookie', methods=['GET', 'POST'])
def getCookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome' +"\n"+ name + '</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=8000)
