from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    x = "Hello world"
    y = "hello"
    z = "1  2  3"
    print(x.lower().strip().split())
    print(y.lower().strip().split())
    print(z.lower().strip().split())