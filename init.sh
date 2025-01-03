#!/bin/bash

# Ensure the script is run with sudo privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit
fi

# List of packages to check and install
packages=("libwebp-dev" "fbi" "python3" "python3-pip")

# Loop through the packages and install if not already installed
for pkg in "${packages[@]}"; do
  if ! dpkg -l | grep -qw $pkg; then
    echo "$pkg not found. Installing $pkg..."
    apt-get install -y $pkg
  else
    echo "$pkg is already installed."
  fi
done

# Set up the Python virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install Python packages from requirements.txt
echo "Installing required Python packages..."
pip install -r requirements.txt

# Run the Python script
echo "Running the Python script..."
python3 main.py
