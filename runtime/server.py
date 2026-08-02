from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from pathlib import Path

# Ensure project root is on path when running this script
ROOT = Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0, str(ROOT))

from execution.agent import agent
from core.config import config

app = Flask(__name__, static_folder=str(ROOT / 'frontend' / 'static'))
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/ask', methods=['POST'])
def api_ask():
    data = request.get_json(force=True)
    message = data.get('message') if isinstance(data, dict) else None
    if not message:
        return jsonify({'error': 'No message provided.'}), 400

    try:
        response = agent.run(message)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    port = int(os.environ.get('PORT', config.get('http_port', 8080) if isinstance(config, dict) else 8080))
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() in ('1', 'true', 'yes')
    app.run(host='0.0.0.0', port=port, debug=debug, use_reloader=debug)
