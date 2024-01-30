import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def parse_sitemap(url):
    # Make a request to the sitemap URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the XML content
        root = ET.fromstring(response.content)

        # Extract data from the sitemap
        urls = [element.text for element in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

        return urls
    else:
        print("Error:", response.status_code)
        print("Error Message:", response.text)
        return []


def parse_content(url):
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract content data by selecting elements with class 'tsr-row'
        # content_data = [div for div in soup.find_all('div', class_='content-wrapper')]
        content_data = []
        for div in soup.find_all('div', class_='content-wrapper'):
            if div.text.strip() == "":
                continue
            if div.text.find("Согласно законодательства Республики Узбекистан, при необходимости, срок рассмотрения") != -1:
                continue
            if div.text.find("Здесь вы можете оставить свои комментарии и замечания по качеству") != -1:
                continue
            content_data.append(div)

        # get first element with class 'tsr-row'
        # content_data = soup.find('div', class_='tsr-row').text

        return content_data
    else:
        print("Error:", response.status_code)
        print("Error Message:", response.text)
        return []


# URL of the sitemap
sitemap_url = "https://www.ucell.uz/sitemap.xml"

# Parse the sitemap and get the list of URLs
parsed_urls = parse_sitemap(sitemap_url)

# Parse content for each URL
news = {
    "title": {
        "uz": "",
        "ru": "",
        "en": "",
    },
    "description": {
        "uz": "",
        "ru": "",
        "en": "",
    },
    "published_date": "",
    "status": 1,
}
for url in parsed_urls:

    if url.find("/myucell/press_srv/") == -1:
        continue
    print(url)
    #
    #     content_data = parse_content(url)
    #
    #     # print(content_data)
    #     # Print the parsed content data
    #     if len(content_data) != 1:
    #         print(f"Parsing content for {url}")
    #         print(f"Parsed Content Data count: {len(content_data)}")
    # for data in content_data:
    #     print("--------------------")
    #     print(data)
    #     print("--------------------")
    #
    # break
