from selenium import webdriver  # type: ignore
from selenium.webdriver.chrome.options import Options  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
import time


def fill_form(data):
    print("🧪 Simulating form fill with data:", data)

    chrome_options = Options()
    # Optional: for headless mode
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")

    # Setting path to the ChromeDriver if not in PATH
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # ✅ Practice-test-link
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

        time.sleep(2)  # Waiting for the page to load
        # For visual confirmation
        driver.save_screenshot("form_test_screenshot.png")

        # We can later add automation here (e.g., filling name, selecting gender, etc.) after getting the actual link.
        print("✅ Test page opened and screenshot taken.")
        return "Form opened and simulated."

    except Exception as e:
        print("❌ Error during Selenium test:", str(e))
        return f"❌ Form fill failed: {e}"

    finally:
        driver.quit()
