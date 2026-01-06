import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import os

def sleep(min=1, max=3):
    time.sleep(random.uniform(min, max))

driver = uc.Chrome()
driver.get("https://www.delfi.lv/zinas")

wait = WebDriverWait(driver, 10)

# Grab headlines and links
headlineElems = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "headline__title")))
headlinesLinks = []
for elem in headlineElems:
    try:
        a = elem.find_element(By.TAG_NAME, "a")
        text = a.text
        href = a.get_attribute("href")
        if text and href:
            headlinesLinks.append((text, href))
    except:
        continue

# Pick 3 random headlines
sample = random.sample(headlinesLinks, min(3, len(headlinesLinks)))

baseFolder = "final_project/delfi_articles"
os.makedirs(baseFolder, exist_ok=True)

#go to each and save
for i, (headlineText, link) in enumerate(sample, 1):
    foldePath = os.path.join(baseFolder, str(i))
    os.makedirs(foldePath, exist_ok=True)

    with open(os.path.join(foldePath, "info.txt"), "w", encoding="utf-8") as f:
        f.write(f"Headline: {headlineText}\nLink: {link}\n")

    driver.get(link)
    sleep(2, 5)

    try:
        article = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "main")))
        with open(os.path.join(foldePath, "text.txt"), "w", encoding="utf-8") as f:
            f.write(article.text)
    except:
        print(f"Could not get article text for {link}")

    sleep(1, 3)

driver.quit()