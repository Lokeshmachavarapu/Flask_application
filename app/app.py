from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

APP_VERSION = "2.1.0"
ENV_STATUS = os.getenv("APP_ENV", "Development")

@app.route('/')
def home():
    return render_template('index.html', version=APP_VERSION, environment=ENV_STATUS)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy", "version": APP_VERSION}), 200

# 🌟 NEW API ENDPOINT ADDED HERE (No other files changed!)
@app.route('/api/v1/tools')
def get_tools():
    return jsonify({
        "project": "Flask CI/CD Pipeline",
        "tools_used": ["Jenkins", "Docker", "Trivy", "GitHub Webhooks", "AWS EC2"],
        "status": "fully_automated"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
