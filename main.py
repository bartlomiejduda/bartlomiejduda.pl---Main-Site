from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def homepage():
    rand_seed = random.randint(0, 100000)
    return render_template("index.html", title="HOME PAGE", seed=rand_seed)

if __name__ == "__main__":
    app.run()