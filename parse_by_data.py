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

        content_data = list()
        # li_obj = dict()
        for items in soup.find('div', class_='sitemap').find("ul"):
            if items.text.strip() == "":
                continue
            for item in items.find_all("li"):
                li_obj = dict(
                    name=item.text.strip(),
                    url=item.find("a").get("href")
                )
                content_data.append(li_obj)

        return content_data
    else:
        print("Error:", response.status_code)
        print("Error Message:", response.text)
        return []


def save_to_json_file(data):
    """
    Save data to file
    :param data:
    :return:
    """
    import json
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == '__main__':
    # URL of the sitemap
    sitemap_url = "https://www.ucell.uz/uz/sitemap"

    # Parse the sitemap and get the list of URLs
    content_data = parse_page(sitemap_url)
    print(content_data)
    # Save the data to a file
    save_to_json_file(content_data)
