from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db
from routes import create_user, send_message, add_contact

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize the database
db.init_app(app)
migrate = Migrate(app, db)

# Register the routes
app.add_url_rule('/create_user', 'create_user', create_user, methods=['POST'])
app.add_url_rule('/send_message', 'send_message', send_message, methods=['POST'])
app.add_url_rule('/add_contact', 'add_contact', add_contact, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)