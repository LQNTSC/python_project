#code = utf-8
import flask

def log(func):
    def wrap():
        print 'before calliing', func.__name__
        func()
        print 'after calliing', func.__name__
    return wrap;

@log
def hello():
    print 'hello'

if __name__ == '__main__':
    hello()