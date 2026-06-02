from bs4 import BeautifulSoup
import requests

URL_PATH_FIXED_PREFIX = 'https://lishi.tianqi.com/'
URL_SEPARATOR_CHAR = '/'


class HomePageSoup:
    def __init__(self, home_page_path: str):
        self.url = URL_PATH_FIXED_PREFIX
        self.home_page_content = None
        self.home_page_path = home_page_path
        self.city_index_url_list = []
        self.city_name_list = []

    def parse(self):
        # parse home page
        if self.home_page_content != '':
            soup = BeautifulSoup(self.home_page_content, 'lxml')
            a_list = soup.select('.tablebox table .table_list li a')
            for a in a_list:
                next_url = a['href']
                if next_url.startswith('/'):
                    self.city_index_url_list.append(next_url[1:-1])
                    self.city_name_list.append(next_url[1:next_url.index('/', 1)])
                else:
                    self.city_index_url_list.append(next_url)
                    self.city_name_list.append(next_url[1:next_url.index('/')])
                pass
            print(self.city_index_url_list)
            print(self.city_name_list)
            pass
        pass

    def crawling_next_page(self):
        for city_name in self.city_name_list:
            index_page = CityIndexPageSoup(city_name, None)
            index_page.read()
            break
            pass
        pass

    def download(self):
        source_html = HistoryWeatherPageCrawling(self.url)
        self.home_page_content = source_html.request_website()
        pass

    def save(self):
        pass

    def read(self):
        if self.url != '':
            self.download()
            self.parse()
            self.crawling_next_page()
            pass
        elif self.home_page_path != '':
            file = open(self.home_page_path, 'r', encoding='utf-8')
            self.home_page_content = file.read()
            file.close()
            pass
        pass


class CityIndexPageSoup:
    def __init__(self, city_name: str, index_page_path: str):
        self.city_index_url = URL_PATH_FIXED_PREFIX + city_name + URL_SEPARATOR_CHAR + 'index.html'
        self.index_page_content = None
        self.index_page_path = index_page_path
        self.city_name = city_name
        self.history_date_list = []

    def parse(self):
        # parse home page
        if self.index_page_content != '':
            soup = BeautifulSoup(self.index_page_content, 'lxml')
            option_list = soup.select('.linegraphtitle .optionbox option')
            for option in option_list:
                history_date = option['value']
                if history_date == '':
                    continue
                self.history_date_list.append(history_date)
                pass
            print(self.history_date_list)
            pass
        pass

    def download(self):
        source_html = HistoryWeatherPageCrawling(self.city_index_url)
        self.index_page_content = source_html.request_website()
        pass

    def save(self):
        pass

    def crawling_next_page(self):
        for history_date in self.history_date_list:
            index_page = CityHistoryPageSoup(self.city_name, history_date, None)
            index_page.read()
            break
            pass
        pass

    def read(self):
        if self.city_index_url != '':
            self.download()
            self.parse()
            self.crawling_next_page()
            pass
        elif self.index_page_path != '':
            file = open(self.index_page_path, 'r', encoding='utf-8')
            self.index_page_content = file.read()
            file.close()
            pass
        pass


class CityHistoryPageSoup:
    def __init__(self, city_name, city_month: str, city_month_page_path: str):
        self.city_month_url = URL_PATH_FIXED_PREFIX + city_name + URL_SEPARATOR_CHAR + city_month + '.html'
        self.city_name = city_name
        self.city_month = city_month
        self.city_month_page_content = None
        self.city_month_page_path = city_month_page_path
        self.history_date_weather_list = []

    def parse(self):
        # parse home page
        if self.city_month_page_content != '':
            soup = BeautifulSoup(self.city_month_page_content, 'lxml')
            city_history_weather_list = soup.select('.tian_three .thrui li')
            for city_history_weather in city_history_weather_list:
                self.history_date_weather_list.append(city_history_weather)
                pass
            # print(self.history_date_weather_list)

            for city_history_weather in city_history_weather_list:
                divs = city_history_weather.find_all('div')
                date = divs[0].text.strip()
                high = divs[1].text.strip()
                low = divs[2].text.strip()
                weather = divs[3].text.strip()
                wind = divs[4].text.strip()
                print(date, high, low, weather, wind)
                pass
            pass
        pass

    def download(self):
        source_html = HistoryWeatherPageCrawling(self.city_month_url)
        self.city_month_page_content = source_html.request_website()
        pass

    def save(self):
        pass

    def post_month_data(self):
        pass

    def read(self):
        if self.city_month_url != '':
            self.download()
            self.parse()
            pass
        elif self.city_month_page_path != '':
            file = open(self.city_month_page_path, 'r', encoding='utf-8')
            self.city_month_page_content = file.read()
            file.close()
            pass
        pass


class HistoryWeatherPageCrawling:
    def __init__(self, url: str):
        self.url = url

    def request_website(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        else:
            return None
