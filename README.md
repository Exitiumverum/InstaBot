# Instagram Bot

A Python-based Instagram bot for educational purposes that can automatically follow followers of a target account.

## ⚠️ Important Disclaimer

This bot is created **ONLY for educational purposes**. Please be aware that:

- Using automation tools on Instagram may violate their Terms of Service
- Instagram has sophisticated detection systems for bot activity
- Your account could potentially be flagged, limited, or banned
- Use this bot at your own risk and responsibility
- This is for learning purposes only - do not use for commercial or malicious purposes

## Features

- 🔐 Secure login to Instagram
- 👥 Extract followers from a target account
- ➕ Automatically follow users
- ⏱️ Random delays to simulate human behavior
- 📊 Comprehensive logging
- 🛡️ Anti-detection measures
- ⚙️ Configurable settings
- 🪟 Cross-platform support (Windows, Linux, macOS)

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- Instagram account
- Target Instagram account (whose followers you want to follow)

## 🚀 Quick Installation

### Windows Users
1. **Download and extract** the project files
2. **Double-click** `install.bat` and follow the prompts
3. **Edit** `config.env` with your credentials
4. **Run** `python run_bot.py`

### Linux/macOS Users
1. **Download and extract** the project files
2. **Run** `./install.sh` in terminal
3. **Edit** `config.env` with your credentials
4. **Run** `python3 run_bot.py`

## 📋 Manual Installation

### 1. Clone or Download
```bash
git clone <repository-url>
cd InstaBot
```

### 2. Install Dependencies

**Windows:**
```cmd
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
# For systems with externally managed Python (like Kali Linux)
pip install -r requirements.txt --break-system-packages

# For regular systems
pip install -r requirements.txt
```

### 3. Set Up Configuration
```bash
# Copy the example config
cp config.env.example config.env
```

### 4. Edit Configuration
Edit `config.env` with your credentials:
```env
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
TARGET_ACCOUNT=target_account_username
MAX_FOLLOWS_PER_SESSION=50
DELAY_BETWEEN_ACTIONS=3
DELAY_BETWEEN_SESSIONS=3600
```

### 5. Test Setup
```bash
# Windows
python test_setup.py

# Linux/macOS
python3 test_setup.py
```

## Configuration Options

| Variable | Description | Default |
|----------|-------------|---------|
| `INSTAGRAM_USERNAME` | Your Instagram username | Required |
| `INSTAGRAM_PASSWORD` | Your Instagram password | Required |
| `TARGET_ACCOUNT` | Target account username | Required |
| `MAX_FOLLOWS_PER_SESSION` | Maximum follows per session | 50 |
| `DELAY_BETWEEN_ACTIONS` | Delay between actions (seconds) | 3 |
| `DELAY_BETWEEN_SESSIONS` | Delay between sessions (seconds) | 3600 |

## Usage

### Method 1: User-Friendly Launcher (Recommended)
```bash
# Windows
python run_bot.py

# Linux/macOS
python3 run_bot.py
```

### Method 2: Direct Execution
```bash
# Windows
python instagram_bot.py

# Linux/macOS
python3 instagram_bot.py
```

### Method 3: Package Installation
```bash
# Install as a package
pip install -e .

# Run using console scripts
instagram-bot
run-instagram-bot
test-instagram-bot
```

## How It Works

1. **Login**: The bot logs into your Instagram account using Selenium
2. **Extract Followers**: Navigates to the target account and extracts their followers
3. **Follow Users**: Systematically follows each follower with random delays
4. **Safety Measures**: Includes various anti-detection features

## Safety Features

- **Random Delays**: Simulates human behavior with random timing
- **User Agent Spoofing**: Uses realistic browser user agent
- **Anti-Detection**: Removes automation indicators
- **Rate Limiting**: Configurable limits to avoid being flagged
- **Error Handling**: Graceful handling of various Instagram UI changes
- **Multiple Selectors**: Robust element detection with fallback strategies

## Logging

The bot creates detailed logs in `instagram_bot.log` including:
- Login attempts and results
- Follower extraction progress
- Follow actions and results
- Errors and exceptions

## Troubleshooting

### Common Issues

1. **Login Failed**
   - Check your credentials in config.env
   - Ensure your Instagram account is not locked
   - Try logging in manually first

2. **Chrome Driver Issues**
   - The bot automatically downloads the correct Chrome driver
   - Make sure Chrome browser is installed
   - Update Chrome to the latest version

3. **Element Not Found**
   - Instagram's UI may have changed
   - Check the logs for specific error messages
   - The bot includes fallback selectors

4. **Rate Limiting**
   - Reduce `MAX_FOLLOWS_PER_SESSION`
   - Increase `DELAY_BETWEEN_ACTIONS`
   - Wait longer between sessions

5. **Windows-Specific Issues**
   - Run Command Prompt as Administrator if needed
   - Ensure Python is added to PATH during installation
   - Use `python` instead of `python3` on Windows

6. **Linux-Specific Issues (Kali Linux)**
   - Use `--break-system-packages` flag with pip
   - Install system packages: `sudo apt install python3-selenium python3-requests python3-bs4 python3-lxml python3-dotenv`
   - Install webdriver-manager: `pip install webdriver-manager --break-system-packages`

### Getting Help

If you encounter issues:
1. Check the log file for detailed error messages
2. Ensure all dependencies are installed correctly
3. Verify your Instagram credentials
4. Make sure the target account is public or you're following it
5. Run `python3 test_setup.py` to verify your setup

## Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| Windows 10/11 | ✅ Full Support | Use `install.bat` or manual installation |
| Linux (Ubuntu/Debian) | ✅ Full Support | Use `install.sh` or manual installation |
| macOS | ✅ Full Support | Use `install.sh` or manual installation |
| Kali Linux | ✅ Full Support | Use system packages + pip for webdriver-manager |

## Legal and Ethical Considerations

- **Terms of Service**: Instagram's ToS prohibit automation
- **Account Safety**: Your account could be at risk
- **Respectful Use**: Don't spam or harass users
- **Educational Purpose**: This is for learning only

## Contributing

This is an educational project. Feel free to:
- Report bugs
- Suggest improvements
- Add new features
- Improve documentation

## License

This project is for educational purposes only. Use responsibly and at your own risk.

## Support

For educational support and questions, please refer to the troubleshooting section above. # InstaBot
