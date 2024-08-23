import requests
from bs4 import BeautifulSoup
import re

BASE_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.5",
}

def yellowstoneAnglerReport(url:str) -> str:
    print(f"In Yellowstone angler Function. URL to report:\n {url}")

def danBailysReport(url:str) -> str:
    print(f"In Dan Bailys Function. URL to report:\n {url}")


def bozemanFlySupplyReport(url:str) -> str:

    try:
        response = requests.get(url, headers=BASE_HEADERS)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"
    
    try:
        soup = BeautifulSoup(response.text, 'html.parser')

         # Extract date from <h> tags using regex
        date_pattern = re.compile(r'\b(?:\d{1,2}\s)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},?\s\d{4}\b')
        date_text = "No date found."

        for header_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headers = soup.find_all(header_tag)
            for header in headers:
                header_text = header.get_text(strip=True)
                date_match = date_pattern.search(header_text)
                if date_match:
                    date_text = date_match.group(0)
                    break
            if date_text != "No date found.":
                break

        items = soup.find_all('div', class_='_1140-w-wrapper padding-top')
        fishing_report = []

        fishing_report.append(date_text)
        for item in items:
            report = item.find('div', class_='text-rich-text w-richtext').get_text()
            formatted_report = [sentence.strip() for sentence in re.split(r'[.!?]', report) if sentence]
            fishing_report.extend(formatted_report)
        return '.\n'.join(fishing_report)
    except Exception as e:
        return f"Error Parsing content: {e}"
    
def riversEdgeReport(url:str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"

    try:
        soup = BeautifulSoup(response.text, 'html.parser')

        items = soup.find_all('div', class_='rich-text__text featured_text')
        temp = items[0].get_text().split('.')
        fishing_report = []

        for item in temp:
            item = item.strip()
            fishing_report.append(f"{item}.")

        return '\n'.join(fishing_report)
    except Exception as e:
        return f"Error Parsing content: {e}"
    
def montanaAnglersReport(url: str) -> str:
    try:
        response = requests.get(url, headers=BASE_HEADERS)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"
    
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract paragraph information from webpage
        paragraphs = soup.find_all('p', {'dir': 'ltr'})
        all_text = [p.get_text(strip=True) for p in paragraphs]
        paragraph_text = '\n'.join(all_text)
        
        # Search for dates using a regular expression
        date_pattern = re.compile(r'\b(?:\d{1,2}\s)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},?\s\d{4}\b')
        page_text = soup.get_text()
        date_match = date_pattern.search(page_text)
        
        date_text = date_match.group(0) if date_match else "No date found."

        return f"Date: {date_text}\n\n{paragraph_text}"
    except Exception as e:
        return f"Error Parsing content: {e}"
    
def yellowDogReport(url: str) -> str:
    try:
        # Send a GET request to the URL
        response = requests.get(url, headers=BASE_HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the date and fishing report from the HTML
        date = soup.find('div', class_='reportContent__date')  
        report = soup.find('div', class_='reportContent__text')  

        date_text = date.get_text(strip=True)
        report_text = report.get_text(strip=True)

        fishing_report = f"Date: {date_text}\n\nFishing Report:\n{report_text}"
        return fishing_report
        
    except requests.exceptions.RequestException as e:
        return {
            'error': str(e)
        }