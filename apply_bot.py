# apply_bot.py
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r'D:\\ARUN\\projects\\autoapply\\chromedriver-win64\\chromedriver.exe'

def init_driver():
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    # Use non-headless for demo
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def apply_to_job(driver, job):
    link = job['Job Link']
    title = job['Title']
    company = job['Company']
    try:
        driver.get(link)
        time.sleep(3)  # Let page load

        # Attempt to find and click an "Apply" button
        apply_buttons = driver.find_elements(By.XPATH, 
            '//button[contains(text(),"Apply") or contains(text(),"apply")] | //a[contains(text(),"Apply")]')

        if apply_buttons:
            apply_buttons[0].click()
            time.sleep(2)

            print(f"Applied: {title} - {company}")
            return True
        else:
            print(f"Apply button not found (skipped): {title} - {company}")
            return False
    except Exception as e:
        print(f"Error applying to job {title} at {company}: {e}")
        return False

def main():
    driver = init_driver()
    applied_count = 0
    skipped_count = 0
    with open("jobs.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        jobs = list(reader)

    for job in jobs:
        success = apply_to_job(driver, job)
        if success:
            applied_count += 1
        else:
            skipped_count += 1

    driver.quit()

    print("\nApply Bot Summary:")
    print(f"Total Jobs Processed: {len(jobs)}")
    print(f"Total Applied: {applied_count}")
    print(f"Total Skipped: {skipped_count}")

if __name__ == "__main__":
    main()
