from flask import render_template, flash, redirect, request, session, abort
from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class student(db.Model):
  id = db.Column('sutent_id',db.Integer, primary_key=True)
  codigo = db.Column(db.String(20), primary_key=True)
  name = db.Column(db.String(100), index=True, unique=True)
  resp = db.Column(db.String(100), index=True, unique=True)
  parent = db.Column(db.String(20), index=True, unique=True)
  ender = db.Column(db.String(120), index=True, unique=True)
  city = db.Column(db.String(30), index=True, unique=True)
  telef = db.Column(db.String(30), index=True, unique=True)
  teleff = db.Column(db.String(30), index=True, unique=True)
  email = db.Column(db.String(50), index=True, unique=True)

  def __init__(self, codigo, name, resp, parent, ender, city, telef, teleff, email):
    self.codigo = codigo
    self.name = name
    self.resp = resp
    self.parent = parent
    self.ender = ender
    self.city = city
    self.telef = telef
    self.teleff = teleff
    self.email = email


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

@app.route('/')
def show_all():
   return render_template('alunos.html', sutent = sutent.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['codigo'] or not request.form['name'] or not request.form['resp'] or not request.form['ender']:
         flash('Please enter all the fields', 'error')
      else:
         sutent = student(request.form['codigo'], request.form['name'],
            request.form['resp'], request.form['parent'],
            request.form['ender'], request.form['city'],
            request.form['telef'],request.form['teleff'], 
            request.form['email'])
         
         db.session.add(sutent)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('alunos_show'))
   return render_template('cadastro.html')
