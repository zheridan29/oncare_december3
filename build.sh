#!/usr/bin/env bash
set -o errexit

# Install system dependencies required for pmdarima compilation
apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    libatlas-base-dev \
    liblapack-dev \
    libblas-dev \
    || echo "System dependencies installation failed, continuing..."

# Upgrade pip and install wheel
pip install --upgrade pip wheel setuptools

# Install numpy and scipy first (pmdarima dependencies)
pip install numpy scipy

# Install all requirements
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate