from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return "Hello World!"
#
# @app.route('/user/<string:name>/<int:id>')
# def user(name, id):
#     return "User_page" + name + '-' + id


@app.route('/about')
def about():
    return "About Us"


@app.route('/home_work')
def home_work():
    return "Is that home work correct?"

if __name__ == '__main__':
    app.run(debug=True)
