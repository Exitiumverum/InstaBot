@echo off
REM Instagram Bot Installation Script for Windows
REM This script installs the Instagram bot and its dependencies

echo 🤖 Instagram Bot Installer
echo ==========================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH. Please install Python 3.7 or higher.
    pause
    exit /b 1
)

REM Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% found

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip is not installed. Please install pip.
    pause
    exit /b 1
)

echo 📦 Installing dependencies...

REM Install dependencies
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully

REM Create config file if it doesn't exist
if not exist "config.env" (
    echo 📝 Creating config.env file...
    copy config.env.example config.env
    echo ✅ config.env created from template
    echo ⚠️  Please edit config.env with your Instagram credentials
) else (
    echo ✅ config.env already exists
)

echo.
echo 🎉 Installation completed successfully!
echo.
echo Next steps:
echo 1. Edit config.env with your Instagram credentials
echo 2. Run: python test_setup.py (to test the setup)
echo 3. Run: python run_bot.py (to start the bot)
echo.
echo 📚 For more information, see README.md
pause 