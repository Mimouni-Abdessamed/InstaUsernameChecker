import time
import pickle
import random
import string
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Instagram URLs
INSTAGRAM_LOGIN_URL = "https://www.instagram.com/accounts/login/"
INSTAGRAM_PROFILE_URL = "https://www.instagram.com/{}/"

# Configure Chrome to avoid detection
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--log-level=3")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
# options.add_argument("--headless")  # Uncomment to run in background

driver = uc.Chrome(options=options)

def login():
    """Logs into Instagram using user-provided credentials."""
    username = input("📌 Enter your Instagram username: ")
    password = input("🔑 Enter your Instagram password: ")

    print("🔑 Opening Instagram login page...")

    driver.get(INSTAGRAM_LOGIN_URL)
    time.sleep(random.uniform(5, 8))  

    try:
        username_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "password")

        # Type like a human (character by character)
        for char in username:
            username_input.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))

        for char in password:
            password_input.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))

        password_input.send_keys(Keys.RETURN)
        print("🔄 Logging in...")

        # Wait for possible reCAPTCHA
        print("⚠️ If there's a reCAPTCHA, solve it manually.")
        time.sleep(60)  # Wait for manual solving

        input("✅ Press ENTER after solving the CAPTCHA to continue...")

        # Wait for homepage
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//nav")))

        # Save session cookies
        with open("session.pkl", "wb") as f:
            pickle.dump(driver.get_cookies(), f)

        print("✅ Logged in & session saved!")

    except Exception as e:
        print(f"❌ Login failed: {e}")

def load_session():
    """Loads session cookies to avoid re-login."""
    try:
        with open("session.pkl", "rb") as f:
            cookies = pickle.load(f)

        driver.get("https://www.instagram.com")  
        time.sleep(random.uniform(3, 6))  

        for cookie in cookies:
            driver.add_cookie(cookie)

        driver.refresh()
        time.sleep(random.uniform(3, 5))

        print("✅ Session restored!")
        return True

    except FileNotFoundError:
        print("❌ No session found! Logging in...")
        return False

def generate_username(length=5):
    """Generates a valid Instagram username of variable length."""
    if length < 3 or length > 30:
        print("⚠️ Username length must be between 3 and 30 characters. Defaulting to 5.")
        length = 5  

    letters_digits = string.ascii_lowercase + string.digits  # Allowed letters & numbers
    special_chars = "._"  # Allowed special characters

    # Ensure the first and last character is a letter or number
    first_char = random.choice(string.ascii_lowercase + string.digits)
    middle_chars = ''.join(random.choices(letters_digits + special_chars, k=length - 2))
    last_char = random.choice(string.ascii_lowercase + string.digits)

    username = first_char + middle_chars + last_char

    # Ensure no consecutive special characters
    while ".." in username or "._" in username or "_." in username or "__" in username:
        middle_chars = ''.join(random.choices(letters_digits + special_chars, k=length - 2))
        username = first_char + middle_chars + last_char

    return username

def check_username(username):
    """Checks if an Instagram username is available."""
    print(f"🔍 Checking '{username}'...")

    driver.get(INSTAGRAM_PROFILE_URL.format(username))
    time.sleep(random.uniform(4, 7))  

    try:
        page_source = driver.page_source

        if "Sorry, this page isn't available." in page_source:
            print(f"✅ '{username}' is AVAILABLE! 💰")
            with open("available_usernames.txt", "a") as f:
                f.write(username + "\n")
            return True

        print(f"❌ '{username}' is TAKEN!")

    except Exception as e:
        print(f"⚠️ Error checking '{username}': {e}")

    return False

def main():
    if not load_session():
        login()

    username_length = int(input("📏 Enter the desired username length (3-30): "))

    while True:
        username = generate_username(username_length)
        check_username(username)
        time.sleep(random.uniform(10, 20))  # Human-like delay to avoid detection

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"🔥 Fatal Error: {e}")
    finally:
        driver.quit()  # Clean exit
