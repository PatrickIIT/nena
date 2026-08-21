import io
import pickle
import torch
import numpy as np
from PIL import Image
import open_clip

# Load CLIP model and embeddings database
device = "cuda" if torch.cuda.is_available() else "cpu"
model, _, preprocess = open_clip.create_model_and_transforms(
    "ViT-B-32", pretrained="openai"
)
model = model.to(device)
model.eval()

with open("models/embeddings_db.pkl", "rb") as f:   # <-- put your file here
    embeddings_db = pickle.load(f)

def predict_sign_from_frame(frame_bytes: bytes, threshold: float = 0.25) -> dict:
    try:
        img = Image.open(io.BytesIO(frame_bytes)).convert("RGB")
        tensor = preprocess(img).unsqueeze(0).to(device)

        with torch.no_grad():
            query_embedding = model.encode_image(tensor)
            query_embedding = query_embedding / query_embedding.norm(dim=-1, keepdim=True)
            query_vec = query_embedding.cpu().numpy()[0]

        best_word, best_score = None, -1.0
        for word, prototype in embeddings_db.items():
            score = float(np.dot(query_vec, prototype))
            if score > best_score:
                best_score, best_word = score, word

        if best_word and best_score >= threshold:
            return {
                "token": best_word.lower(),
                "display_text": best_word,
                "confidence": round(best_score, 3),
                "model_version": "sign-0.1.0",
                "accepted": True,
            }
        else:
            return {
                "token": None,
                "display_text": None,
                "confidence": round(best_score, 3),
                "model_version": "sign-0.1.0",
                "accepted": False,
            }
    except Exception as e:
        return {"error": str(e)}
