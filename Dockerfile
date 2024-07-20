FROM python:3.8-slim-buster

# Switch to root user
USER root

# Create application directory
RUN mkdir /app

# Copy all files to /app directory
COPY . /app/

# Set working directory to /app
WORKDIR /app

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Airflow
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW__CORE__DAGBAG_IMPORT_TIMEOUT=1000
ENV AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True

# Update and install necessary packages
RUN apt-get update -y && apt-get install -y sudo

# Make the start script executable
RUN chmod +x /app/start.sh

# Set entrypoint to the start script
ENTRYPOINT ["/bin/sh"]

# Run the start script
CMD ["/app/start.sh"]
