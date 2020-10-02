from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#####################
# 여기에 코드 적기!

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = 'articles'
ws1.append(['제목', '링크', '신문사'])


for article in articles:
    title = article.select_one('dl > dt > a').text
    url = article.select_one('dl > dt > a')['href']
    comp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사','')
    # sp_nws6 > dl > dd.txt_inline > span._sp_each_source

    ws1.append([title, url, comp])

#####################

driver.quit()
wb.save(filename='articles.xlsx')