#!/usr/bin/env bash
set -o errexit

# Upgrade pip and install wheel first
pip install --upgrade pip wheel setuptools

# Install Cython first (required for pmdarima build)
pip install Cython

# Install numpy and scipy with compatible versions (pmdarima may not support numpy 2.x)
pip install "numpy<2.0" "scipy<2.0"

# Install other build dependencies that pmdarima needs
pip install "pandas>=0.19" "scikit-learn>=0.22" "statsmodels>=0.13.2" "joblib>=0.11"

# Now install pmdarima separately (it will use the already-installed dependencies)
pip install pmdarima==2.0.4

# Install all other requirements (excluding pmdarima to avoid reinstall)
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate