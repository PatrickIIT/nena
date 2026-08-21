FROM python:3.11-slim

WORKDIR /app
COPY backend/api /app

RUN pip install flask pillow torch torchvision transformers open_clip_torch

ENV PORT=5000
CMD ["python", "app.py"]
