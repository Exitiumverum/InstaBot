import os
import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv('config.env')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('instagram_bot.log'),
        logging.StreamHandler()
    ]
)

class InstagramBot:
    def __init__(self):
        self.driver = None
        self.username = os.getenv('INSTAGRAM_USERNAME')
        self.password = os.getenv('INSTAGRAM_PASSWORD')
        self.target_account = os.getenv('TARGET_ACCOUNT')
        self.max_follows = int(os.getenv('MAX_FOLLOWS_PER_SESSION', 50))
        self.delay_between_actions = int(os.getenv('DELAY_BETWEEN_ACTIONS', 3))
        self.delay_between_sessions = int(os.getenv('DELAY_BETWEEN_SESSIONS', 3600))
        
        if not all([self.username, self.password, self.target_account]):
            raise ValueError("Please set all required environment variables in config.env")
    
    def setup_driver(self):
        """Setup Chrome driver with appropriate options"""
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Add user agent to appear more human-like
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Execute script to remove webdriver property
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        return self.driver
    
    def random_delay(self, min_delay=1, max_delay=3):
        """Add random delay to simulate human behavior"""
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)
    
    def login(self):
        """Login to Instagram"""
        try:
            logging.info("Starting Instagram login process...")
            self.driver.get("https://www.instagram.com/")
            self.random_delay(2, 4)
            
            # Wait for login form to appear
            wait = WebDriverWait(self.driver, 10)
            
            # Find and fill username
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.clear()
            for char in self.username:
                username_field.send_keys(char)
                time.sleep(0.1)
            
            self.random_delay(1, 2)
            
            # Find and fill password
            password_field = self.driver.find_element(By.NAME, "password")
            password_field.clear()
            for char in self.password:
                password_field.send_keys(char)
                time.sleep(0.1)
            
            self.random_delay(1, 2)
            
            # Click login button
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            
            # Wait for login to complete
            self.random_delay(3, 5)
            
            # Handle "Save Login Info" dialog if it appears
            try:
                not_now_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
                )
                not_now_button.click()
                self.random_delay(2, 3)
            except:
                logging.info("No 'Save Login Info' dialog found")
            
            # Handle "Turn on Notifications" dialog if it appears
            try:
                not_now_notifications = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']"))
                )
                not_now_notifications.click()
                self.random_delay(2, 3)
            except:
                logging.info("No notifications dialog found")
            
            logging.info("Successfully logged in to Instagram")
            return True
            
        except Exception as e:
            logging.error(f"Login failed: {str(e)}")
            return False
    
    def get_followers(self, account_username):
        """Get followers of a specific account"""
        try:
            logging.info(f"Getting followers for account: {account_username}")
            
            # Navigate to the target account
            self.driver.get(f"https://www.instagram.com/{account_username}/")
            self.random_delay(3, 5)
            
            # Try different selectors for followers link
            followers_link = None
            followers_selectors = [
                "//a[contains(@href, '/followers/')]",
                "//a[contains(@href, '/followers')]",
                "//a[text()='followers']",
                "//a[contains(text(), 'followers')]",
                "//a[contains(@href, 'followers')]",
                # Try to find by text content
                "//a[contains(., 'followers')]",
                "//a[contains(., 'Followers')]"
            ]
            
            for selector in followers_selectors:
                try:
                    followers_link = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    logging.info(f"Found followers link with selector: {selector}")
                    break
                except:
                    continue
            
            if not followers_link:
                logging.error("Could not find followers link")
                return []
            
            followers_link.click()
            self.random_delay(2, 3)
            
            # Wait for followers modal to load
            wait = WebDriverWait(self.driver, 10)
            followers_modal = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
            )
            
            followers = []
            last_height = self.driver.execute_script("return arguments[0].scrollHeight", followers_modal)
            
            # Scroll to load more followers
            while len(followers) < 200:  # Limit to 200 followers for safety
                # Scroll down
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_modal)
                self.random_delay(2, 3)
                
                # Get current followers with multiple selector strategies
                follower_elements = []
                
                # Strategy 1: Look for links with role="link"
                try:
                    follower_elements = followers_modal.find_elements(By.XPATH, ".//a[@role='link']")
                except:
                    pass
                
                # Strategy 2: Look for links with href containing usernames
                if not follower_elements:
                    try:
                        follower_elements = followers_modal.find_elements(By.XPATH, ".//a[contains(@href, '/')]")
                    except:
                        pass
                
                # Strategy 3: Look for elements with Instagram-specific classes
                if not follower_elements:
                    try:
                        follower_elements = followers_modal.find_elements(By.XPATH, ".//a[contains(@class, '_a6hd')]")
                    except:
                        pass
                
                # Process found elements
                for element in follower_elements:
                    try:
                        href = element.get_attribute('href')
                        if href and '/p/' not in href and '/reel/' not in href:
                            # Extract username from href
                            username = href.split('/')[-2] if href.endswith('/') else href.split('/')[-1]
                            if username and username != account_username and username not in followers:
                                # Additional validation - check if it looks like a username
                                if len(username) > 0 and not username.startswith('http'):
                                    followers.append(username)
                    except:
                        continue
                
                # Check if we've reached the end
                new_height = self.driver.execute_script("return arguments[0].scrollHeight", followers_modal)
                if new_height == last_height:
                    break
                last_height = new_height
            
            # Try different methods to close the modal
            try:
                # Method 1: Try the close button with aria-label
                close_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Close']")
                close_button.click()
            except:
                try:
                    # Method 2: Try close button with X icon
                    close_button = self.driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Close')]")
                    close_button.click()
                except:
                    try:
                        # Method 3: Try SVG close icon
                        close_button = self.driver.find_element(By.XPATH, "//svg[@aria-label='Close']")
                        close_button.click()
                    except:
                        try:
                            # Method 4: Try ESC key
                            from selenium.webdriver.common.keys import Keys
                            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
                            logging.info("Closed modal using ESC key")
                        except:
                            # Method 5: Try clicking outside the modal
                            try:
                                self.driver.find_element(By.XPATH, "//div[@role='dialog']//..").click()
                                logging.info("Closed modal by clicking outside")
                            except:
                                logging.warning("Could not close modal automatically, continuing anyway")
            
            logging.info(f"Found {len(followers)} followers")
            return followers[:100]  # Return first 100 followers
            
        except Exception as e:
            logging.error(f"Error getting followers: {str(e)}")
            return []
    
    def follow_user(self, username):
        """Follow a specific user"""
        try:
            logging.info(f"Attempting to follow: {username}")
            
            # Navigate to user's profile
            self.driver.get(f"https://www.instagram.com/{username}/")
            self.random_delay(2, 4)
            
            # Check if already following with multiple selectors
            already_following = False
            following_selectors = [
                "//button[text()='Following']",
                "//button[contains(text(), 'Following')]",
                "//button[@aria-label='Following']",
                "//button[contains(@aria-label, 'Following')]",
                "//div[contains(@class, '_aad6') and contains(text(), 'Following')]",
                "//div[contains(@class, '_aade') and contains(text(), 'Following')]"
            ]
            
            for selector in following_selectors:
                try:
                    following_button = self.driver.find_element(By.XPATH, selector)
                    logging.info(f"Already following {username}")
                    already_following = True
                    break
                except:
                    continue
            
            if already_following:
                return False
            
            # Try different selectors for follow button based on actual Instagram HTML
            follow_button = None
            follow_selectors = [
                # New Instagram selectors based on actual HTML
                "//button[contains(@class, '_aswp') and contains(@class, '_aswr')]",
                "//div[contains(@class, '_aad6') and contains(text(), 'Follow')]",
                "//div[contains(@class, '_aade') and contains(text(), 'Follow')]",
                "//button[.//div[contains(@class, '_aad6') and contains(text(), 'Follow')]]",
                "//button[.//div[contains(@class, '_aade') and contains(text(), 'Follow')]]",
                # Fallback selectors
                "//button[text()='Follow']",
                "//button[contains(text(), 'Follow')]",
                "//button[@aria-label='Follow']",
                "//button[contains(@aria-label, 'Follow')]",
                "//button[contains(@class, 'follow')]"
            ]
            
            for selector in follow_selectors:
                try:
                    follow_button = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, selector))
                    )
                    logging.info(f"Found follow button with selector: {selector}")
                    break
                except:
                    continue
            
            if not follow_button:
                logging.error(f"Could not find follow button for {username}")
                return False
            
            follow_button.click()
            
            logging.info(f"Successfully followed {username}")
            return True
            
        except Exception as e:
            logging.error(f"Error following {username}: {str(e)}")
            return False
    
    def run_bot(self):
        """Main bot execution"""
        try:
            logging.info("Starting Instagram Bot...")
            
            # Setup driver
            self.setup_driver()
            
            # Login
            if not self.login():
                logging.error("Failed to login. Exiting...")
                return
            
            # Get followers of target account
            followers = self.get_followers(self.target_account)
            
            if not followers:
                logging.error("No followers found. Exiting...")
                return
            
            # Follow users
            followed_count = 0
            for username in followers:
                if followed_count >= self.max_follows:
                    logging.info(f"Reached maximum follows limit ({self.max_follows})")
                    break
                
                if self.follow_user(username):
                    followed_count += 1
                
                # Random delay between follows
                self.random_delay(self.delay_between_actions, self.delay_between_actions + 2)
            
            logging.info(f"Bot completed. Followed {followed_count} users.")
            
        except Exception as e:
            logging.error(f"Bot error: {str(e)}")
        
        finally:
            if self.driver:
                self.driver.quit()
                logging.info("Browser closed")

if __name__ == "__main__":
    bot = InstagramBot()
    bot.run_bot() 