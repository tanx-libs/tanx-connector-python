#!/bin/bash

# This script installs the "@tanx-libs/tanx-connector" package using npm

# Print a message indicating the installation process
echo "Installing @tanx-libs/tanx-connector..."

# Run npm install command
npm i @tanx-libs/tanx-connector

# Check the exit status of the npm command
if [ $? -eq 0 ]; then
    echo "Installation successful!"
else
    echo "Installation failed. Please check your npm configuration and try again."
fi
