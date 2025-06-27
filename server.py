# server.py
from flask import Flask, jsonify
from main import run_newsletter

app = Flask(__name__)

@app.route("/generate-newsletter", methods=["POST"])
def generate_newsletter():
    try:
        html_output = run_newsletter()
        return jsonify({"status": "success", "message": "Newsletter generated and sent", "html": html_output}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000, debug=True)
