#!/usr/bin/env bash
set -o errexit

# Upgrade pip and install wheel first
pip install --upgrade pip wheel setuptools

# Install Cython first (required for pmdarima build)
pip install Cython

# Install numpy and scipy with compatible versions (pmdarima may not support numpy 2.x)
pip install "numpy" "scipy"

# Install other build dependencies that pmdarima needs
pip install "pandas>=0.19" "scikit-learn>=0.22" "statsmodels>=0.13.2" "joblib>=0.11"

# Now install pmdarima with --no-build-isolation so it uses the installed dependencies
pip install pmdarima

# Install all other requirements (excluding pmdarima to avoid reinstall)
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate