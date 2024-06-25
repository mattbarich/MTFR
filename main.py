import requests
from bs4 import BeautifulSoup

bfs = "https://www.bozemanflysupply.com/river-report/gallatin"




def scrape_data():
    response = requests.get(bfs)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='_1140-w-wrapper padding-top')
    fishing_report = []

    for item in items:
        river = item.find('h1', class_='inline mobile-text-size').get_text()
        report = item.find('div', class_='text-rich-text w-richtext').get_text()

        fishing_report.append(f"{river}: {report}")
    return '\n'.join(fishing_report)



if __name__ == "__main__":
    data = scrape_data()
    print(data)