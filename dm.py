#!/d/sysutils/conda/python
# -*- coding: utf-8 -*-

from selenium import webdriver

# selenium에서 사용할 웹 드라이버 절대 경로 정보
chromedriver = 'D:\\webdriver\chromedriver.exe'
# selenum의 webdriver에 앞서 설치한 chromedirver를 연동한다.
driver = webdriver.Chrome(chromedriver)
# driver로 특정 페이지를 크롤링한다.
driver.get('https://www.gov.kr/nlogin/?curr_url=/mw%2FAA040OfferMainFrm.do%3Fcapp_biz_cd%3D15000000098%26tp_seq%3D')

print("+" * 100)
print(driver.title)   # 크롤링한 페이지의 title 정보
print(driver.current_url)  # 현재 크롤링된 페이지의 url
print("건축물대장 크롤링")
print("-" * 100)


