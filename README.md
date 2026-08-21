# NENA Backend API

## Run locally
pip install -r requirements.txt
python backend/api/app.py

## Endpoints
- GET /health
- POST /v1/sign/predict (multipart JPEG)
- POST /v1/speech/transcribe (multipart WAV/M4A)

## Deployment
docker build -t nena-backend .
docker run -p 5000:5000 nena-backend
