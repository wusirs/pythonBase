# 吞噬星空小说
# https://www.ibiquge.la/7/7928/index.html
import re
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
    tsxk_url = 'https://www.ibiquge.la/7/7928/index.html'
    home_page_html = request_website(tsxk_url)
    soup = BeautifulSoup(home_page_html, 'lxml')
    title_a = soup.select('.box_con #list dl dd')
    title_list = []
    for title_dd in title_a:
        title_list.append({
            'title': title_dd.a.get_text(),
            'url': 'https://www.ibiquge.la/' + title_dd.a['href']
        })
    text_list = []
    for i in title_list:
        print(i['title'])
        detail_page_html = request_website(i['url'])
        # soup = BeautifulSoup(home_page_html, 'lxml')
        # content = soup.select('#content')
        p = r'id="content">(.*?)<p>'  # 正则只获取正文
        texts = re.findall(p, detail_page_html)[0]
        texts = texts.replace('<br />', '').replace('&nbsp;', '').replace('\\r\\r', '\n')
        text_list.append(str(i['title']) + '\n\n' + texts)
    return text_list


def save_to_txt(text_list: list):
    f = open('吞噬星空.txt', 'a', encoding='UTF-8')
    for i in text_list:
        f.write(str(i))
    f.flush()
    f.close()


if __name__ == '__main__':
    text_list = query_hero_info()
    save_to_txt(text_list)
