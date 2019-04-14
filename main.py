from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("TESTE.html")

@app.route('/<int:id>', methods=['GET', 'POST'])
def buscJSON():
    if request.method == 'POST':
        post = request.form['number']
        response = requests.get("https://jsonplaceholder.typicode.com/posts"+post)
        content = json.loads(response.content)
        return render_template("TESTE2.html", content=content)
    else:
        return render_template('TESTE2.html')

if __name__ == "__main__":
    app.run(debug=True)