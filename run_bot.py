#!/usr/bin/env python3
"""
Instagram Bot Launcher
A simple interface to run the Instagram bot with safety checks
"""

import os
import sys
import time
from datetime import datetime

def check_prerequisites():
    """Check if all prerequisites are met"""
    print("🔍 Checking prerequisites...")
    
    # Check if config file exists
    if not os.path.exists('config.env'):
        print("❌ config.env file not found!")
        print("   Please copy config.env.example to config.env and add your credentials")
        return False
    
    # Check if required packages are installed
    try:
        import selenium
        import webdriver_manager
        import dotenv
        print("✅ All required packages are installed")
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("   Please run: pip install -r requirements.txt")
        return False
    
    return True

def show_warning():
    """Show important warning about using the bot"""
    print("\n" + "="*60)
    print("⚠️  IMPORTANT WARNING ⚠️")
    print("="*60)
    print("This Instagram bot is for EDUCATIONAL PURPOSES ONLY!")
    print("")
    print("⚠️  Using automation tools on Instagram may:")
    print("   • Violate Instagram's Terms of Service")
    print("   • Result in account suspension or banning")
    print("   • Trigger security measures")
    print("")
    print("⚠️  Use at your own risk!")
    print("⚠️  This is for learning purposes only!")
    print("")
    print("="*60)
    
    response = input("Do you understand and accept the risks? (yes/no): ").lower().strip()
    return response in ['yes', 'y']

def get_bot_settings():
    """Get bot settings from user"""
    print("\n🤖 Bot Settings")
    print("-" * 30)
    
    # Load current settings from config
    from dotenv import load_dotenv
    load_dotenv('config.env')
    
    current_max_follows = os.getenv('MAX_FOLLOWS_PER_SESSION', '50')
    current_delay = os.getenv('DELAY_BETWEEN_ACTIONS', '3')
    target_account = os.getenv('TARGET_ACCOUNT', 'Not set')
    
    print(f"Target account: {target_account}")
    print(f"Current max follows per session: {current_max_follows}")
    print(f"Current delay between actions: {current_delay} seconds")
    
    # Ask if user wants to modify settings
    modify = input("\nDo you want to modify these settings for this session? (yes/no): ").lower().strip()
    
    if modify in ['yes', 'y']:
        try:
            new_max = input(f"Max follows per session (current: {current_max_follows}): ").strip()
            if new_max:
                os.environ['MAX_FOLLOWS_PER_SESSION'] = new_max
            
            new_delay = input(f"Delay between actions in seconds (current: {current_delay}): ").strip()
            if new_delay:
                os.environ['DELAY_BETWEEN_ACTIONS'] = new_delay
                
        except KeyboardInterrupt:
            print("\n❌ Cancelled by user")
            return False
    
    return True

def run_bot():
    """Run the Instagram bot"""
    print("\n🚀 Starting Instagram Bot...")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    try:
        from instagram_bot import InstagramBot
        
        # Create and run bot
        bot = InstagramBot()
        bot.run_bot()
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Bot error: {e}")
        print("Check the log file for more details")

def main():
    """Main launcher function"""
    print("Instagram Bot Launcher")
    print("=" * 30)
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Please fix the issues above.")
        return
    
    # Show warning
    if not show_warning():
        print("\n❌ Bot execution cancelled by user.")
        return
    
    # Get bot settings
    if not get_bot_settings():
        print("\n❌ Bot execution cancelled by user.")
        return
    
    # Countdown
    print("\n🔄 Starting bot in 5 seconds...")
    for i in range(5, 0, -1):
        print(f"   {i}...")
        time.sleep(1)
    
    # Run bot
    run_bot()
    
    print("\n✅ Bot execution completed!")
    print("📋 Check instagram_bot.log for detailed logs")

if __name__ == "__main__":
    main() 