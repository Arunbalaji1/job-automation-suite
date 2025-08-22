from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv

# Your chromedriver path
chrome_driver_path = r'D:\\ARUN\\projects\\autoapply\\chromedriver-win64\\chromedriver.exe'

def init_driver():
    options = webdriver.ChromeOptions()
    # Spoof user agent to appear as a real browser
    user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36")
    options.add_argument(f'user-agent={user_agent}')
    # Avoid headless to reduce detection risk
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def human_sleep(min_sec=2, max_sec=5):
    time.sleep(random.uniform(min_sec, max_sec))

def scrape_remoteok_jobs(driver, keyword="python"):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    driver.get(url)

    print("Waiting for jobs to load...")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tr.job"))
        )
    except Exception as e:
        print("Timeout waiting for job rows:", e)
        return []

    job_rows = driver.find_elements(By.CSS_SELECTOR, "tr.job")
    print(f"Found {len(job_rows)} job rows")

    jobs = []
    for job in job_rows:
        try:
            title = job.find_element(By.CSS_SELECTOR, "h2").text.strip()
            company = job.find_element(By.CSS_SELECTOR, ".companyLink").text.strip()
            location_elem = job.find_elements(By.CSS_SELECTOR, ".location")
            location = location_elem[0].text.strip() if location_elem else "Remote"
            job_link = job.get_attribute("data-url")
            if job_link and not job_link.startswith("http"):
                job_link = "https://remoteok.com" + job_link

            jobs.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Job Link": job_link
            })
        except Exception as e:
            print("Error parsing job:", e)
            continue

    return jobs

def save_to_csv(jobs, filename="jobs.csv"):
    with open(filename, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["Title", "Company", "Location", "Job Link"])
        writer.writeheader()
        for job in jobs:
            writer.writerow(job)

def main():
    driver = init_driver()
    try:
        jobs = scrape_remoteok_jobs(driver, keyword="python")
        save_to_csv(jobs)
        print(f"Scraped {len(jobs)} jobs. Saved to jobs.csv")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
