from wtforms import  TextField, TextAreaField, SubmitField,validators
from flask.ext.wtf import Form
class ContactForm(Form):
  name = TextField("Name",  [validators.Required("Please enter your name")])
  email = TextField("Email",  [validators.Required("Please enter your email"),validators.Email("Please enter your email address")])
  subject = TextField("Subject",  [validators.Required("Please enter a subject ")])
  message = TextAreaField("Message",  [validators.Required("Please enter your a message")])
  submit = SubmitField("Send")