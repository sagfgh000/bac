from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Backend is running!"

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    video_url = data.get('video_url')
    if not video_url:
        return jsonify({"error": "No video URL provided"}), 400

    # Simulated processing (replace this with real processing)
    tags = ["car", "sunset", "road"]  # fake tags
    return jsonify({
        "video_url": video_url,
        "tags": tags
    })

if __name__ == '__main__':
    app.run(debug=True)