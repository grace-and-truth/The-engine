from flask import Blueprint, render_template, request, jsonify

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        # store or forward message later via webhook
        return jsonify({'status': f'Message received from {name}'})
    return render_template('contact.html')