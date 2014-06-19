# from flask import Flask, render_template,request,flash
# from forms import ContactForm
# from flask.ext.mail import Message,Mail
# from intro_to_flask import app


from intro_to_flask import app
from flask import render_template, request, flash,session, redirect, url_for
from forms import ContactForm,SignupForm,SigninForm
from flask.ext.mail import Message, Mail
from models import db


mail = Mail()

# app = Flask(__name__) 

# app.secret_key = 'development key'

# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USERNAME"] = 'contact@example.com'
# app.config["MAIL_PASSWORD"] = 'your-password'
# mail.init_app(app)

# @app.route('/testdb')
# def testdb():
#   if db.session.query("1").from_statement("SELECT 1").all():
#     return 'It works.'
#   else:
#     return 'Something is broken.'

@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')
  
@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if 'email' in session:
    return redirect(url_for('profile'))
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
       
      session['email'] = newuser.email
       
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  if 'email' in session:
    return redirect(url_for('profile'))
  form = SigninForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)


@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('home'))


@app.route('/profile')
def profile():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html')


# if __name__ == '__main__':
#   app.run(debug=True)