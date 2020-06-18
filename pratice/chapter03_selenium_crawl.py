# ** chapter03_selenium_crawl.py
# * : selenium을 이용해서 페이지를 크롤링 하는 방법
# *

from selenium import webdriver
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe')


url = 'https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90/'

import time # 우리가사진 떠오고 싶은 데 소스 코드 먼저 가져오고 나중에 웹 브라우저 사진이 떠서 미쳐 소스 코드에 사진 코드가 안따짐 이를 막기 위해
time.sleep(5) # 5초간 waiting. 인터벌 시간을 주는 것

# time.sleep()을 사용하는 이유
# : 웹 드라이버에서 페이지가 완전히 로딩되기 전에 page_source를 가져오기 때문에
#   미완성된 코드로 내용을 수집하는데 한계가 있음 그래서 %초 간의 시간을 주고
#   페이지가 전부 로딩되면 그때 소스를 가져오도록 하기 위함


driver.get(url) # 웹드라이버로 URL 접속

page_code = driver.page_source # 해당 URL의 전체 소스 코드 가져오기
print(page_code) # resp.text 까지 가져 온 것을 확인할 수 있다. 단지 requests를 이용하는 것이 아닌 나만의 웹사이트를 띄워서 가져오는 것~
