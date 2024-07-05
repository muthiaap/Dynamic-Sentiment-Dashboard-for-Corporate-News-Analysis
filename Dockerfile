FROM apache/airflow:latest-python3.11

# Update pip and setuptools
RUN pip install --no-cache-dir --upgrade pip setuptools

# Install system dependencies
USER root
RUN mkdir -p /opt/airflow/cache && chown -R airflow:root /opt/airflow/cache
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-dev \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user
USER airflow

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt