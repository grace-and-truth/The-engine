from flask import Blueprint, render_template, request, jsonify

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/', methods=['GET', 'POST'])
def calendar_view():
    if request.method == 'POST':
        event = request.form.get('event')
        date = request.form.get('date')
        return jsonify({'status': f'Event "{event}" saved for {date}'})
    return render_template('calendar.html')