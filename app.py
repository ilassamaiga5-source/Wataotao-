from flask import os
import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>WATAOTAO BF 🔥</h1><p><a href='/client'>VOIR CLIENT UBER DESIGN</a></p>"

@app.route('/client')
def client():
    return render_template('client.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', port=5000, debug=True)
