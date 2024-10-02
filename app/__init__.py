from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes
    from .routes import main

    # Register Blueprints
    app.register_blueprint(main)

    return app
