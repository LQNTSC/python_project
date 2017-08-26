# -*-encoding=UTF-8 -*-

from newproject import app


@app.route('/')
def index():
    return 'Hello'
if __name__ == '__main__':
    app.run(debug = True)