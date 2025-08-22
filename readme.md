# 🚀 Job Automation Suite

A modular Python Selenium project designed to automate scraping job listings from open job boards and simulate basic job application workflows. This project provides a foundation for automating the end-to-end job search and application process with room for extensibility.

---

## 📋 Table of Contents

- [🧐 Project Overview](#project-overview)  
- [📂 Project Structure](#project-structure)  
- [⚙️ Setup Instructions](#setup-instructions)  
- [🎯 Usage Guide](#usage-guide)  
- [🧩 Core Components](#core-components)  
- [🔧 Extending the Project](#extending-the-project)  
- [⚠️ Limitations and Considerations](#limitations-and-considerations)  
- [📝 Sample Resume Description](#sample-resume-description)  

---

## 🧐 Project Overview

This project automates the following flows:
- 🔍 Scrapes job listings (title, company, location, job link) for a given keyword from job boards such as RemoteOK or We Work Remotely.  
- 🖱️ Simulates application steps by navigating to job pages and interacting with application buttons (stopping short of full form submission in MVP).  
- 🛠️ Orchestrates the entire scraping and application process with console summaries to track progress.

The automation pipeline is structured to facilitate collaborative development and iterative enhancements, relying on CSV files as a simple shared data exchange.

---

## 📂 Project Structure

job-automation-suite/
├── **scraper.py** --> 🕷️ Scrapes job listings and saves them to jobs.csv
├── **apply_bot.py** --> 🤖 Reads jobs.csv and simulates applying to jobs
├── **main.py** --> 🧑💻 Orchestrates the entire workflow (scrape + apply)
└── **jobs.csv** -->  📄 Shared CSV file to transfer job data between components


---

## ⚙️ Setup Instructions

1. **Install Python and Dependencies**

   - Requires Python 3.7+  
   - Install Selenium:
     ```
     pip install selenium
     ```
   - Install Chrome browser if not present.  
   - Download ChromeDriver matching your Chrome version: [🔗 ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)  
   - Place `chromedriver.exe` in a known location and update the driver path in the scripts (`chrome_driver_path`).

2. **Optional**  
   For easier driver management (future use), install `webdriver-manager`:
   ```
     pip install webdriver-manager
     ```

---

## 🎯 Usage Guide

- **Run the full suite:**  
Runs scraper and apply bot sequentially with a summary.

- **Run only the scraper:**  

Scrapes jobs and saves to `jobs.csv`.

- **Run only the apply bot:**  

Reads `jobs.csv` and simulates applications.

---

## 🧩 Core Components

### 📍 Scraper (`scraper.py`)

- Uses Selenium to open a job board URL and search for a keyword (default: "Python").  
- Extracts job Title, Company, Location, and Job Link.  
- Saves results to `jobs.csv`.

### 📍 Apply Bot (`apply_bot.py`)

- Reads job data from `jobs.csv`.  
- Visits each job link, attempts to click "Apply".  
- Stops at “Apply Page Opened Successfully” step; logs success/skips.

### 📍 Orchestrator (`main.py`)

- Runs scraper and then apply bot in order.  
- Prints summaries of jobs scraped and applications processed.

---

## 🔧 Extending the Project

You can enhance by:

- 💾 Using a database (SQLite) instead of CSV for robustness.  
- 🌐 Adding support for multiple job boards.  
- 📝 Automating full application form filling and resume uploads.  
- 🐞 Adding retries, error handling, and logging.  
- 📊 Creating dashboards and reports.  
- 🗓️ Scheduling automated runs with CI/CD tools.

---

## ⚠️ Limitations and Considerations

- ⚠️ Designed for demo and educational use only.  
- 🔍 Scrapers rely on the structure of the target websites; updates may break them.  
- 🛑 Does not (yet) submit real job applications.  
- 📜 Always comply with terms of service and legal guidelines for automated browsing.

---

## 📝 Sample Resume Description

> Developed a Python Selenium automation suite that scrapes job listings from open job platforms, exports data to CSV, and automates basic application navigation workflows, enhancing job search efficiency.

---

## 📬 Contact & Contributions

Contributions, bug reports, and feature requests are welcome via repository issues or pull requests.

---

*This documentation provides a clear and friendly guide for users and collaborators to understand, set up, run, and extend the Job Automation Suite efficiently.*

