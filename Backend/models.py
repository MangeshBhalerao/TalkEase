from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

#User model
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),unique=True,nullable=False)
    google_id = db.Column(db.String(256),unique=True,nullable = True)
    email = db.Column(db.String(100),unique=True,nullable = False)

    message_sent = db.relationship('Message',foreign_keys='Message.sender_id')
    message_received = db.relationship('Message',foreign_keys='Message.receiver_id')

    contacts = db.relationship('Contact',foreign_keys='Contact.user_id')

    def __repr__(self):
        return f"<User {self.username}>"
    
#Message for chat message    
class Message(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    sender = db.relationship('User', foreign_keys=[sender_id])
    receiver = db.relationship('User', foreign_keys=[receiver_id])

    def __repr__(self):
        return f"<Message {self.content[:20]}>"
    
#Contact    
class Contact(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    user = db.relationship('User', foreign_keys=[user_id])
    contact = db.relationship('User', foreign_keys=[contact_id])

    def __repr__(self):
        return f"<Contact {self.user.username} - {self.contact.username}>"