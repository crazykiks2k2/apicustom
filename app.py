from flask import Flask

app = Flask(__name__)

@app.route('/say_hello', methods=['GET'])
def say_hello():
    print("Hello")
    return "Hello printed!"

if __name__ == '__main__':
    app.run(debug=True)
