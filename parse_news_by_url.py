"""
Parse content by URL
"""
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json


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

        article = soup.find('article', class_='ucl-section-breadcrumbs')
        next_article_element = article.find_next('article')
        next_div_element = next_article_element.find_next('div', class_='tsr-container')
        title_next_div_element = next_div_element.find_next('div', class_='tsr-container')
        content = title_next_div_element.find_next('div', class_='content-wrapper').find('div', class_='tsr-row')
        title = title_next_div_element.text.strip()

        content_data = dict(
            title=title,
            content=str(content)
        )
        return content_data
    else:
        print("Error:", response.status_code)
        print("Error Message:", response.text)
        return []


def save_to_json_file(data, idx):
    """
    Save data to file
    :param data:
    :return:
    """
    import json
    # file encoding utf-8
    with open(f'parsed_news_2_3_{idx}.json', 'w', encoding='utf-8') as outfile:
        # save to file
        json.dump(data, outfile, ensure_ascii=False)


if __name__ == '__main__':
    # URL of the sitemap
    base_url = "https://www.ucell.uz"

    # Read data from file parsing_news_urls.json
    with open('parsing_news_urls.json') as json_file:
        data = json.load(json_file)
        news_list = list()
        idx = 0
        for url in data["corporate"]["types"]["urls_2"]:
            idx += 1
            print(idx, url)
            content_data = parse_page(base_url + url)
            url_uz = url.replace("/ru/", "/uz/")
            content_data_uz = parse_page(base_url + url_uz)
            url_en = url.replace("/ru/", "/en/")
            content_data_en = parse_page(base_url + url_en)
            slug = url.split("/")[-1]
            day = url.split("/")[5]
            month = url.split("/")[4]
            year = url.split("/")[3]
            published_date = f"{year}-{month}-{day}"
            cd_news = dict(
                slug=slug,
                published_date=published_date,
                uz=content_data_uz,
                ru=content_data,
                en=content_data_en
            )
            news_list.append(cd_news)
            #
            # if idx == 2:
            #     break
            # if idx % 50 == 0:
            #     print(idx)
        save_to_json_file(news_list, idx)
                # break
