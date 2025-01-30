from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def serve_home():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
