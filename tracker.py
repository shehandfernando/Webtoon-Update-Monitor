import requests
from bs4 import BeautifulSoup
from plyer import notification
import os

# --- CONFIGURATION ---
# Replace this with the actual URL of the manga/manhwa series page
MANHWA_URL = "https://example-scanlation-site.com/manga/eleceed/"
# The CSS selector for the element containing the latest chapter number/title
CHAPTER_CSS_SELECTOR = ".latest-chapter-list li a span.chapter-name"
SERIES_NAME = "Eleceed"
SAVE_FILE = "last_chapter.txt"

def get_latest_chapter():
    """Scrapes the target URL for the latest chapter."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(MANHWA_URL, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        chapter_element = soup.select_one(CHAPTER_CSS_SELECTOR)
        
        if chapter_element:
            return chapter_element.text.strip()
        else:
            print("Could not find the chapter element. Check your CSS selector.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def send_notification(series, chapter):
    """Sends a desktop notification."""
    notification.notify(
        title=f"New {series} Chapter!",
        message=f"Chapter {chapter} is now available to read.",
        app_name="Chapter Tracker",
        timeout=10 # Notification stays for 10 seconds
    )

def main():
    print(f"Checking for updates: {SERIES_NAME}...")
    latest_chapter = get_latest_chapter()
    
    if not latest_chapter:
        return

    # Read the last known chapter from our save file
    last_known_chapter = ""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            last_known_chapter = f.read().strip()

    # Compare and notify
    if latest_chapter != last_known_chapter:
        print(f"Update found! {latest_chapter}")
        send_notification(SERIES_NAME, latest_chapter)
        
        # Save the new chapter so we don't get notified again
        with open(SAVE_FILE, "w") as f:
            f.write(latest_chapter)
    else:
        print(f"No new chapters. Last checked: {latest_chapter}")

if __name__ == "__main__":
    main()