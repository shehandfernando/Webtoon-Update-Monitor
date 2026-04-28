# Webtoon Update Monitor

A lightweight Python automation script that tracks web pages for new manga/manhwa chapter releases and pushes desktop notifications to your machine. As a huge fan of manga and manhwa—particularly action, Murim, and Wuxia series—I built this tool to ensure I never miss a drop. 

By default, the script includes configuration examples for tracking *Eleceed* and *Legend of the Northern Blade*, and the logic is structured to work smoothly with sources like `comick.live`.

## 🚀 Getting Started

### Prerequisites
You need Python 3.x installed along with a few external libraries. Install them via pip:
`pip install requests beautifulsoup4 plyer`

### Running the Tracker
1. Open your terminal or command prompt.
2. Navigate to the project directory.
3. Run the script:
`python tracker.py`

## ⚙️ Configuration
Because website structures vary, you must configure the script for your specific reading source. Open `tracker.py` and modify the `--- CONFIGURATION ---` section:
* **MANHWA_URL**: The direct link to the series page.
* **CHAPTER_CSS_SELECTOR**: The exact HTML/CSS path to the latest chapter text. You can find this by right-clicking the chapter on the website, selecting "Inspect", and copying the selector.

## 🛠️ Features
* **Headless Web Scraping:** Uses `requests` and `BeautifulSoup` to parse HTML and extract specific data points quietly.
* **State Management:** Writes to a local `last_chapter.txt` file to remember the last checked release, preventing spam.
* **Native Desktop Notifications:** Uses `plyer` to trigger OS-level toast notifications when a new update is detected.

## ⚖️ License
This project is licensed under the MIT License.