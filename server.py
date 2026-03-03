from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
from instagram_bot import run_bot

# Use absolute paths based on this file's location,
# so Gunicorn works regardless of working directory.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static",
    template_folder=BASE_DIR
)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-bot", methods=["POST"])
def execute_bot():
    print("Iniciando ejecución del bot vía API...")
    results = run_bot()
    return jsonify(results)

@app.route("/screenshots/<path:filename>")
def get_screenshot(filename):
    return send_from_directory(BASE_DIR, filename)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    print(f"Servidor iniciado en http://localhost:{port}")
    app.run(host="0.0.0.0", port=port)
