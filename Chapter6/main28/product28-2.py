from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/1', methods=['GET'])
def firstPage():
    return "First Page OK"    

@app.route('/2', methods=['GET'])
def secondPage():
    return "Second Page OK"

def main():
    app.run(debug=True, port=80)

if __name__ == '__main__':
    main()
