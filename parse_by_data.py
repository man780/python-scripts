"""
Parse content by data.json
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


def read_json_file(file_name):
    """
    Read data from file
    :param file_name:
    :return:
    """
    import json
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data


if __name__ == '__main__':
    pages = read_json_file("data.json")
    i = 0
    for page in pages:
        page_url = page['url'].removeprefix("/uz")
        if page_url.find("/myucell/press_srv") != -1:
            continue
        if page_url.find("/subscribers/tariffs/") != -1:
            """Tariffs"""
            i += 1
            print(i, page_url)
        elif page_url.find("/subscribers/services2/") != -1:
            """Services"""
            i += 1
            print(i, page_url)

        # content_data = parse_page(url["url"])
        # print(content_data)
    # content_data = parse_page(sitemap_url)
    # print(content_data)
    # Save the data to a file
    # save_to_json_file(content_data)
