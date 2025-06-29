# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Configuration
```bash
cp config.env.example config.env
```

Edit `config.env` with your credentials:
```env
INSTAGRAM_USERNAME=your_instagram_username
INSTAGRAM_PASSWORD=your_instagram_password
TARGET_ACCOUNT=target_account_username
```

### 3. Test Setup
```bash
python test_setup.py
```

### 4. Run the Bot
```bash
python run_bot.py
```

## 📋 What You Need

- **Instagram Account**: Your own account for the bot to use
- **Target Account**: The account whose followers you want to follow
- **Google Chrome**: The bot uses Chrome for automation
- **Python 3.7+**: Make sure you have Python installed

## ⚠️ Important Notes

- This is for **educational purposes only**
- Use at your own risk
- Instagram may detect and ban automated activity
- Start with small numbers (10-20 follows per session)
- Use longer delays between actions (5-10 seconds)

## 🔧 Troubleshooting

If you get errors:

1. **"Chrome driver not found"**: The bot will download it automatically
2. **"Login failed"**: Check your credentials in config.env
3. **"Element not found"**: Instagram's UI may have changed
4. **"Rate limited"**: Reduce MAX_FOLLOWS_PER_SESSION and increase delays

## 📊 Monitoring

- Check console output for real-time progress
- View detailed logs in `instagram_bot.log`
- The bot will show you exactly what it's doing

## 🛡️ Safety Tips

- Don't run the bot too frequently
- Use realistic delays between actions
- Monitor your account for any warnings
- Stop immediately if you get any Instagram warnings

---

**Remember**: This is for learning web automation, not for gaining followers! 