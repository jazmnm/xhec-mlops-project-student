docker build -t abalone_age_prediction -f Dockerfile.app .
docker run -dp 0.0.0.0:8000:8001 abalone_age_prediction
