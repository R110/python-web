from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/test/<search_query>')
def search(search_query):
    return search_query
def int_type(value):
    print(value+1)
    return 'correct'

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return 'correct'

@app.route("/name/<name>")
def index(name):
    if name.lower() == "jed":
        return "hello {}".format(name), 200
    else:
        return "not found", 404

if __name__ == 'main':
    app.run()

