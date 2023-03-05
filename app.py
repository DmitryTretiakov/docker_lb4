from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return "Hello, world!"

if name == "main":
    app.run(debug=True, host='0.0.0.0', port=80)
