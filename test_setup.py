#!/usr/bin/env python3
"""
Test script to verify Instagram bot setup
"""

import sys
import importlib

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'selenium',
        'webdriver_manager',
        'dotenv',
        'requests',
        'bs4',
        'lxml'
    ]
    
    print("Testing package imports...")
    failed_imports = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    return failed_imports

def test_bot_import():
    """Test if the Instagram bot can be imported"""
    print("\nTesting Instagram bot import...")
    try:
        from instagram_bot import InstagramBot
        print("✅ InstagramBot class imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import InstagramBot: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error importing InstagramBot: {e}")
        return False

def test_config_file():
    """Test if config file exists"""
    import os
    print("\nTesting configuration...")
    
    if os.path.exists('config.env'):
        print("✅ config.env file found")
        return True
    else:
        print("⚠️  config.env file not found")
        print("   Please copy config.env.example to config.env and add your credentials")
        return False

def main():
    """Run all tests"""
    print("Instagram Bot Setup Test")
    print("=" * 30)
    
    # Test Python version
    print(f"Python version: {sys.version}")
    
    # Test imports
    failed_imports = test_imports()
    
    # Test bot import
    bot_import_success = test_bot_import()
    
    # Test config
    config_exists = test_config_file()
    
    # Summary
    print("\n" + "=" * 30)
    print("Test Summary:")
    
    if not failed_imports and bot_import_success:
        print("✅ All imports successful")
    else:
        print("❌ Some imports failed")
        if failed_imports:
            print(f"   Failed packages: {', '.join(failed_imports)}")
            print("   Run: pip install -r requirements.txt")
    
    if config_exists:
        print("✅ Configuration file found")
    else:
        print("⚠️  Configuration file missing")
        print("   Run: cp config.env.example config.env")
        print("   Then edit config.env with your credentials")
    
    if not failed_imports and bot_import_success and config_exists:
        print("\n🎉 Setup looks good! You can run the bot with:")
        print("   python instagram_bot.py")
    else:
        print("\n🔧 Please fix the issues above before running the bot")

if __name__ == "__main__":
    main() 