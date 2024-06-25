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
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='rich-text__text featured_text')
    fishingReport = []

    for item in items:
        report = item.get_text()
        print("Report given: " + report + "\n")
        # fishingReport.append(f"Report: ", {report})

    return '\n'.join(fishingReport)

def montanaAnglersReport(url: str) -> str:
    print("In Monatana Anglers Function in gallatin.py")
    print(url)

def yellowDogReport(url: str) -> str:
    print("In Yellow Dogs Function in gallatin.py")
    print(url)