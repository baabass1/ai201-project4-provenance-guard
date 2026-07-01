from flask import Flask
from routes.submit import submit_bp
from routes.logs import logs_bp
from utils.extensions import limiter
from routes.appeal import appeal_bp

app = Flask(__name__)

limiter.init_app(app)

app.register_blueprint(submit_bp)
app.register_blueprint(logs_bp)
app.register_blueprint(appeal_bp)

@app.route("/")
def home():
    return "Provenance Guard API is running!"

if __name__ == "__main__":
    app.run(debug=True)