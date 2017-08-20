#code = utf-8
from flask import Flask, render_template, request, redirect, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'nowcoder'

@app.route('/index/')
@app.route('/')
def index():
    res = ''
    for msg in get_flashed_messages():
        res = res + msg
    res += 'hello'
    return res

@app.route('/profile/<int:uid>/', methods = ['GET', 'post'])
def profile(uid):
    return render_template('profile.html', uid = uid)

@app.route('/request')
def request_demo():
    res = request.args.get('key','defalutkey') + '<br>'
    for property in dir(request):
        res = res + str(property) + '|==|<br>' +  str(eval('request.' + property)) + '<br>'
    return res

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', url = request.url)

@app.route('/login')
def login():
    app.logger.info('log success')
    flash('login sucessful', 'info')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)