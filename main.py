# Se importa Flask, una instancia de esta clase será mi aplicación WSGI
from flask import Flask, url_for, request, render_template
from markupsafe import escape

# Si este archivo se importase como un módulo, el argumento sería "__main__"
app = Flask(__name__)

@app.route('/')
def index():
  return 'Index page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
  return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return 'Inicia sesión'
  else:
    return 'Muestra el formulario de registro'

@app.route('/user/<username>')
def profile(username):
  # show the user profile for that user
  # escape() es un módulo de seguridad que elimina caracteres html
  return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
  #muestra el post con el id obtenido, siendo este un entero.
  return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
  #muestra el subpath despues de /path/
  return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
  return 'The project page'

@app.route('/about')
def about():
  return 'The about page'

# with app.test_request_context():
#   print(url_for('index'))
#   print(url_for('login'))
#   print(url_for('login', next='/'))
#   print(url_for('profile', username='John Doe'))

# url_for('static', filename='style.css')