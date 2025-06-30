from flask import Blueprint, render_template, request
import smtplib, os
from email.mime.text import MIMEText
import openai

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/rephrase', methods=['GET', 'POST'])
def rephrase():
    output = ""
    if request.method == 'POST':
        content = request.form['content']
        format = request.form['format']
        prompt = f"Rephrase the following into a {format}:\n{content}"

        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        output = response['choices'][0]['message']['content']
    return render_template('rephrase.html', output=output)

@main.route('/send-email', methods=['GET', 'POST'])
def send_email():
    message_sent = False
    if request.method == 'POST':
        to_email = request.form['to_email']
        subject = request.form['subject']
        html_body = request.form['html_body']

        msg = MIMEText(html_body, 'html')
        msg['Subject'] = subject
        msg['From'] = os.getenv("EMAIL_FROM")
        msg['To'] = to_email

        with smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
            server.login(os.getenv("EMAIL_FROM"), os.getenv("EMAIL_PASSWORD"))
            server.send_message(msg)
            message_sent = True
    return render_template('email.html', message_sent=message_sent)

@main.route('/calendar')
def calendar():
    return render_template('calendar.html')

@main.route('/contacts')
def contacts():
    return render_template('contacts.html')
