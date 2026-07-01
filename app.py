from flask import Flask
from routes.submit import submit_bp

app = Flask(__name__)

app.register_blueprint(submit_bp)


@app.route("/")
def home():
    return "Provenance Guard API is running!"


if __name__ == "__main__":
    app.run(debug=True)