import requests
from bs4 import BeautifulSoup
import re

def bozemanFlySupplyReport(url:str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"
    
    try:
        soup = BeautifulSoup(response.text, 'html.parser')

        items = soup.find_all('div', class_='_1140-w-wrapper padding-top')
        fishing_report = []

        for item in items:
            report = item.find('div', class_='text-rich-text w-richtext').get_text()

            fishing_report.append(f"Report: {report}")
        return '\n'.join(fishing_report)
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
        report = "Report: "
        report = report + items[0].get_text()
        return report
    except Exception as e:
        return f"Error Parsing content: {e}"


def montanaAnglersReport(url: str) -> str:
    try:
        response = requests.get(url)
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

        return f"Date: {date_text}\n\nReport:\n{paragraph_text}"
    except Exception as e:
        return f"Error Parsing content: {e}"


def yellowDogReport(url: str) -> str:
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract the date and fishing report from the HTML
        date = soup.find('div', class_='reportContent__top')  # Replace with the actual class or identifier
        report = soup.find('div', class_='reportContent__text')  # Replace with the actual class or identifier
        
        # Check if both date and report were found
        if date and report:
            formatted_report = f"Fishing Report for {date.get_text(strip=True)}:\n\n{report.get_text(strip=True)}"
            return formatted_report
        else:
            return {
                'error': 'Could not find the date or the fishing report on the page.'
            }
    
    except requests.exceptions.RequestException as e:
        return {
            'error': str(e)
        }