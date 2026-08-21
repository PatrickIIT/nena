import io
import torch
import whisper

# Load Whisper model (small or medium depending on your resources)
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model = whisper.load_model("small", device=device)  # <-- adjust model size

def transcribe_audio(audio_bytes: bytes) -> dict:
    try:
        # Save audio temporarily
        temp_path = "/tmp/input_audio.wav"
        with open(temp_path, "wb") as f:
            f.write(audio_bytes)

        result = whisper_model.transcribe(temp_path, language="sw")

        text = result.get("text", "").strip()
        tokens = text.lower().split()

        return {
            "text": text,
            "tokens": tokens,
            "language": "sw",
            "model_version": "speech-0.1.0",
        }
    except Exception as e:
        return {"error": str(e)}
