import soupHistoryWeather

# if __name__ == '__main__':
#     home_page_url = ''
#     home_page_content = ''
#     home_page_path = '.\\sourceHtml\\histortWeatherMain.html'
#     homepage = soupHistoryWeather.HomePageSoup(home_page_url, home_page_content, home_page_path)
#     homepage.read()
#     homepage.parse()


# if __name__ == '__main__':
#     city_index_url = ''
#     index_page_path = '.\\sourceHtml\\zhuriheIndex.html'
#     cityIndexPage = soupHistoryWeather.CityIndexPageSoup(city_index_url, index_page_path)
#     cityIndexPage.read()
#     cityIndexPage.parse()


# if __name__ == '__main__':
#     city_month = ''
#     city_month_page_path = '.\\sourceHtml\\zhurihe202605.html'
#     cityHistoryPage = soupHistoryWeather.CityHistoryPageSoup(city_month, city_month_page_path)
#     cityHistoryPage.read()
#     cityHistoryPage.parse()


# if __name__ == '__main__':
#     cityHistoryPage = soupHistoryWeather.HistoryWeatherPageCrawling('https://lishi.tianqi.com/')
#     print(cityHistoryPage.request_website())