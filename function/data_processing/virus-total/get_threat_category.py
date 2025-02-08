import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def crawl(sha256):
    options = Options()
    options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(f"https://www.virustotal.com/gui/file/{sha256}")

        file_view = WebDriverWait(driver, 10).until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "file-view"
        )))
        shadow_root = file_view.shadow_root

        time.sleep(1)
        report = shadow_root.find_element(By.ID, "report")
        time.sleep(1)
        threat = report.find_element(By.CSS_SELECTOR, ".col.hstack.gap-2.text-truncate")

        # threat_category = tab.find_element(By.CSS_SELECTOR, ".badge.rounded-pill.bg-body-tertiary.text-body")
        # print(threat_category.text)

        threat_categories = threat.find_elements(By.CSS_SELECTOR, ".badge.rounded-pill.bg-body-tertiary.text-body")

        categories = None
        if threat_categories:
            categories = [category.text for category in threat_categories]
        return categories
    except Exception as e:
        print(e)
    finally:
        driver.quit()

    return None
