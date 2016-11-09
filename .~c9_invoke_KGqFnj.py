import os
from flask import Flask
from f

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', name="name")

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))