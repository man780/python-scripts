"""
Parse content by URL
"""
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def parse_page(url):
    """
    Parse the HTML content
    :param url:
    :return:
    """
    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        news_items = soup.find('section', class_='tsr-section-news-listing').find("div", class_="tsr-container").find_all("a", class_="tsr-module-news2")

        content_data = list()
        for news_item in news_items:
            content_data.append(news_item.get("href"))

        return content_data
    else:
        print("Error:", response.status_code)
        print("Error Message:", response.text)
        return []

def append_to_json_file(data):
    """
    Save data to file
    :param data:
    :return:
    """
    import json
    with open('news_urls_data.json', 'a') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    # URL of the sitemap
    for i in range(1, 2):
        news_url = f"https://ucell.uz/ru/news?news_type=1"
        content_data = parse_page(news_url)
        print(i, content_data)
        append_to_json_file(content_data)
