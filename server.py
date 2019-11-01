from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello():
  name = request.args.get('name', default = 'world', type = str)
  return "<html><body><h1>Hello " + name + "</h1><p>This is a test paragraph!</p></body></html>"

@app.route('/health')
def health():
  return "OK"

if __name__ == '__main__':
  app.run()