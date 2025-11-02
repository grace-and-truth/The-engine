from flask import Blueprint, request, jsonify, render_template

workflow_bp = Blueprint('workflow', __name__)

@workflow_bp.route('/', methods=['GET'])
def index():
    return render_template('workflows.html')

@workflow_bp.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json
    return jsonify({'status': 'Webhook received', 'data': data})

@workflow_bp.route('/send-webhook', methods=['POST'])
def send_webhook():
    # In next phase, we’ll make this send to other services
    return jsonify({'status': 'Webhook sent (simulated)'})