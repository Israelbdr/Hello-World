from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        post = (request.form['number'])

        if (request.form['userId'] == ''):
            response = requests.get("https://jsonplaceholder.typicode.com/posts/" + post)
            content = response.json()
            return render_template("TESTE2.html", content=content)
        else:
            title = request.form['title']
            body = request.form['body']
            userid = request.form['userId']
            data = {'title':title, 'body':body, 'userId':userid}
            response = requests.post("https://jsonplaceholder.typicode.com/posts/", data)
            content = response.json()
            return render_template("TESTE2.html", content=content)
    return render_template("TESTE.html")

if __name__ == "__main__":
    app.run(debug=True)