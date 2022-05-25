from flask import Flask, request, render_template
from emoji import emojize
import json

app = Flask(__name__)

@app.route("/")
def homepage():
    #https://emoji-translator-2022.uc.r.appspot.com/?name=:snake:&date=today
    name = request.args.get('name', 'World')
    return emojize(f"Hello {name}!!")


@app.route("/all", methods = ['POST', 'GET','DELETE'])
def all():
    #if request.method == 'POST':
    emojis = dict()
    with open('emojis.txt') as f:
        lines = f.readlines()
    for line in lines:
        text = line.strip()
        emojis[text] = emojize(text)
    return json.dumps(emojis, indent=4, ensure_ascii=False)
    jsonify json_data, 202


if __name__ == "__main__":
    app.run(debug=True)
    
