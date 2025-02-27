from flask import request, jsonify
from models import db, User, Message, Contact

# Route to create a new user
def create_user():
    data = request.get_json()
    username = data.get('username')
    google_id = data.get('google_id')
    email = data.get('email')

    # Ensure all required fields are provided
    if not username or not google_id or not email:
        return jsonify({'error': 'Missing required fields'}), 400

    # Create new user
    new_user = User(username=username,google_id=google_id, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user': username}), 201

# Route to send a message
def send_message():
    data = request.get_json()
    sender_id = data['sender_id']
    receiver_id = data['receiver_id']
    content = data['content']

    # Create new message
    new_message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(new_message)
    db.session.commit()

    return jsonify({"message": "Message sent successfully"}), 201

# Route to add a contact
def add_contact():
    data = request.get_json()
    user_id = data['user_id']
    contact_id = data['contact_id']

    # Create new contact relationship
    new_contact = Contact(user_id=user_id, contact_id=contact_id)
    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Contact added successfully'}), 201
