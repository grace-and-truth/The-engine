from flask import Flask, render_template
from .core.rephrase import rephrase_bp
from .core.emailer import emailer_bp
from .core.contact import contact_bp
from .core.calendar import calendar_bp
from .core.workflows import workflows_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(rephrase_bp)
    app.register_blueprint(emailer_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(calendar_bp)
    app.register_blueprint(workflows_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
    