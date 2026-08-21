from flask import Flask
from routes.health import health_bp
from routes.sign import sign_bp
from routes.speech import speech_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    app.register_blueprint(sign_bp)
    app.register_blueprint(speech_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=False)
