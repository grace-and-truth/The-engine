from flask import Blueprint, render_template, request, jsonify

rephrase_bp = Blueprint('rephrase', __name__)

@rephrase_bp.route('/', methods=['GET', 'POST'])
def rephrase_text():
    if request.method == 'POST':
        text = request.form.get('text', '')
        try:
            # Example placeholder logic
            result = text[::-1]  # reverse text for demo
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return render_template('rephrase.html')