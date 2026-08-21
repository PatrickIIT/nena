from flask import Blueprint, request, jsonify
from services.sign_service import predict_sign_from_frame

sign_bp = Blueprint("sign", __name__)

@sign_bp.route("/v1/sign/predict", methods=["POST"])
def predict_sign():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    frame_bytes = file.read()

    result = predict_sign_from_frame(frame_bytes)
    return jsonify(result)
