from flask import Blueprint, render_template, request, jsonify

emailer_bp = Blueprint('email', __name__)

@email_bp.route('/', methods=['GET', 'POST'])
def generate_email():
    if request.method == 'POST':
        subject = request.form.get('subject', '')
        idea = request.form.get('idea', '')
        generated_email = f"Subject: {subject}\n\nHey there! Here's an email about {idea}."
        return jsonify({'email': generated_email})
    return render_template('email.html')