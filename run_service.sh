docker build -t abalone_age_prediction -f Dockerfile.app .
docker run -d -p 0.0.0.0:8000:8001 -p 0.0.0.0:4200:4201 abalone_age_prediction
