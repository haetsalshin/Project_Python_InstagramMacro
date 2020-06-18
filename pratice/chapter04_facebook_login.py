# ** chapter03_facebook_login.py
# * : selenium을 이용해서 페이스북 로그인
# * : 단점 : 지속적으로 사용 불가능... 페이스북이 보안을 위해 로그인 버튼의
# *    선택자를 수시로 변경함 OTL...

from selenium import webdriver

# selenium을 사용해서 facebook에 로그인!
# !! 로그인 버튼은 보안조치 때문에 id값이 자꾸 변동함

path = '..' # 집이나 다른 곳 가서 사용할 시 경로가 달라 질 수 있기 때문에. 이렇게 따로 객체설정 하면 더 편리하다.
driver = webdriver.Chrome(executable_path='{}/webdriver/chromedriver.exe'.format(path))


url = 'https://www.facebook.com/'
driver.get(url) # 웹드라이버로 URL페이지 접속

driver.find_element_by_id('email').send_keys('') #드라이버야 id가 email인 것을 찾아라~ 그리고 거기에 이 값을 넣어라.
driver.find_element_by_id('pass').send_keys('') #드라이버야 id가 pass인 것을 찾아라~ 그리고 거기에 이 값을 넣어라.
driver.find_element_by_id('u_0_e').click() # 드라이브야~ id가 u_0_e를 찾아서 해당 버튼을 클릭해라~