from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/html', methods=['GET'])
def htmlPage():
    return render_template("test.html")

def main():
    app.run(debug=True, port=80)

if __name__ == '__main__':
    main()
