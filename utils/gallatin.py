import requests
import requests
from bs4 import BeautifulSoup

def bozemanFlySupplyReport(url:str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='_1140-w-wrapper padding-top')
    fishing_report = []

    for item in items:
        report = item.find('div', class_='text-rich-text w-richtext').get_text()

        fishing_report.append(f"Report: {report}")
    return '\n'.join(fishing_report)


def riversEdgeReport(url:str) -> str:
   print("In Rivers Edge Function in gallatin.py")

'''
gallatin_urls = ["https://www.bozemanflysupply.com/river-report/gallatin", 
                 "https://theriversedge.com/pages/gallatin-river-fishing-report",
                 "https://www.yellowdogflyfishing.com/pages/gallatin-river-fishing-report",
                 "https://www.montanaangler.com/montana-fishing-report/gallatin-river-fishing-report"]

def getRiverReport(river):
    for url in gallatin_urls:
        utils.process_requests.scrape_data(url)
'''