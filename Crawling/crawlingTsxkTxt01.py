# 吞噬星空小说
# https://www.quanwenyuedu.io/n/tunshixingkong/xiaoshuo.html

import requests
from bs4 import BeautifulSoup


def request_website(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return response.text
    else:
        return None


def query_hero_info():
    tsxk_url = 'https://www.quanwenyuedu.io/n/tunshixingkong/xiaoshuo.html'
    home_page_html = request_website(tsxk_url)
    soup = BeautifulSoup(home_page_html, 'lxml')
    title_a = soup.select('ul li')
    print(title_a)
    title_list = []
    # for title_dd in title_a:
    #     title_list.append({
    #         'title': title_dd.a.get_text(),
    #         'url': 'https://www.ibiquge.la/' + title_dd.a['href']
    #     })
    # for i in title_list:
    #     print(i['url'])
    #     detail_page_html = request_website(i['url'])
    #     soup = BeautifulSoup(home_page_html, 'lxml')
    #     content = soup.select('#content')
    #     print(detail_page_html)
    #     break


def save_to_txt(hero_infos):
    pass


if __name__ == '__main__':
    content = query_hero_info()
    save_to_txt(content)
