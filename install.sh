#!/bin/bash

# Instagram Bot Installation Script
# This script installs the Instagram bot and its dependencies

set -e  # Exit on any error

echo "🤖 Instagram Bot Installer"
echo "=========================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "✅ Python $PYTHON_VERSION found"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "📦 Installing dependencies..."

# Install dependencies
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt --break-system-packages
elif command -v pip &> /dev/null; then
    pip install -r requirements.txt --break-system-packages
else
    echo "❌ Neither pip3 nor pip found. Please install pip."
    exit 1
fi

echo "✅ Dependencies installed successfully"

# Create config file if it doesn't exist
if [ ! -f "config.env" ]; then
    echo "📝 Creating config.env file..."
    cp config.env.example config.env
    echo "✅ config.env created from template"
    echo "⚠️  Please edit config.env with your Instagram credentials"
else
    echo "✅ config.env already exists"
fi

# Make scripts executable
chmod +x run_bot.py
chmod +x test_setup.py

echo ""
echo "🎉 Installation completed successfully!"
echo ""
echo "Next steps:"
echo "1. Edit config.env with your Instagram credentials"
echo "2. Run: python3 test_setup.py (to test the setup)"
echo "3. Run: python3 run_bot.py (to start the bot)"
echo ""
echo "📚 For more information, see README.md" 