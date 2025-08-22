# main.py
import subprocess

def run_scraper():
    print("Starting scraper...")
    result = subprocess.run(["python", "scraper.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Scraper failed.")
        return False
    return True

def run_apply_bot():
    print("Starting apply bot...")
    result = subprocess.run(["python", "apply_bot.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Apply bot failed.")
        return False
    return True

def main():
    if not run_scraper():
        return
    if not run_apply_bot():
        return
    print("Job Automation Suite completed successfully.")

if __name__ == "__main__":
    main()
