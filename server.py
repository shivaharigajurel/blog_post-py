from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    
    random_num = random.randint(1, 10)
    date = datetime.datetime.now().year
    return render_template('index.html', num = random_num, d= date)


@app.route("/<username>")
def name(username):
    gen_response = requests.get(f"https://api.genderize.io/?name={username}")
    data = gen_response.json()
    return render_template('guess.html', name = username, gender= data['gender'])

@app.route("/blog")
def get_blog():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template('blog.html', posts= data)


if __name__ == "__main__":
    app.run(
        debug=True
    )


