from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome(r"C:\Users\Owner\Desktop\sparta\chromedriver.exe") # 웹드라이버 파일의 경로
driver.get("https://www.google.com/search?q=%EB%B0%95%EB%AF%BC%EC%98%81&tbm=isch&ved=2ahUKEwiLrff44JPsAhUFYJQKHdckASsQ2-cCegQIABAA&oq=%EB%B0%95%EB%AF%BC%EC%98%81&gs_lcp=CgNpbWcQAzIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6CAgAELEDEIMBUNecAljdtgJg9rcCaAJwAHgAgAFviAHOCJIBBDExLjGYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABAMABAQ&sclient=img&ei=LPx1X4vnHYXA0QTXyYTYAg&bih=720&biw=768")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!

# thumbnails = soup.select('#imgList > div > a > img')
#imgList > div:nth-child(1) > a > img
thumbnails = soup.select('#islrg > div > div > a.wXeWr > div.bRMDJf > img')
#islrg > div.islrc > div:nth-child(1) > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    if (img == None):
        break
    else:
        dload.save(img, f'imgs_homework/{i}.jpg')
    i+=1
###################################

driver.quit() # 끝나면 닫아주기
