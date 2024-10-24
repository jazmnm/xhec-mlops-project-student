# Make sure to check bin/run_services.sh, which can be used here
# Base image: Python 3.10 slim
FROM python:3.10.15-slim

# Set working directory
WORKDIR /app_home

# Copy the requirements file and install dependencies
COPY ./requirements.txt /app_home/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app_home/requirements.txt

# Copy the web service source code into the container
COPY ./src/web_service /app_home/src/web_service

# Expose the ports for Uvicorn and Prefect
EXPOSE 8001
EXPOSE 4201

# Use the custom run_service.sh script to start both Prefect and Uvicorn
CMD ["bin/run_services.sh"]

# Do not forget to expose the right ports! (Check the PR_4.md)
