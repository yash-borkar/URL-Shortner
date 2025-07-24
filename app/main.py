from flask import Flask, request, jsonify, redirect
from datetime import datetime
import string, random, validators
from threading import Lock
from datetime import datetime, timezone

app = Flask(__name__)
url_store = {}  # short_code -> {url, clicks, created_at}
lock = Lock()

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url or not validators.url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    with lock:
        while True:
            code = generate_code()
            if code not in url_store:
                break
        url_store[code] = {
            "url": original_url,
            "clicks": 0,
            "created_at": datetime.now(timezone.utc).isoformat()

        }

    return jsonify({
        "short_code": code,
        "short_url": f"http://localhost:5000/{code}"
    }), 201

@app.route('/<code>', methods=['GET'])
def redirect_to_url(code):
    with lock:
        entry = url_store.get(code)
        if not entry:
            return jsonify({"error": "Short code not found"}), 404
        entry["clicks"] += 1
        return redirect(entry["url"])

@app.route('/api/stats/<code>', methods=['GET'])
def get_stats(code):
    entry = url_store.get(code)
    if not entry:
        return jsonify({"error": "Short code not found"}), 404
    return jsonify({
        "url": entry["url"],
        "clicks": entry["clicks"],
        "created_at": entry["created_at"]
    })
