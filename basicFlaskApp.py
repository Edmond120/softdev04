from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return '/route1\n/route2'
@my_app.route('/1')
def route1():
	return 'route1'
@my_app.route('/2')
	return 'route2'

if __name__ == '__main__':
    my_app.run()
