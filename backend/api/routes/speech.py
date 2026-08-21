from flask import Blueprint, request, jsonify
from services.speech_service import transcribe_audio

speech_bp = Blueprint("speech", __name__)

@speech_bp.route("/v1/speech/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    file = request.files["file"]
    audio_bytes = file.read()

    result = transcribe_audio(audio_bytes)
    return jsonify(result)
