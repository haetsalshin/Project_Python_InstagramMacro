# ** chapter02_webbrower.py
# * : Selenium의 Webdriver 사용방법(+Chrome Driver)

from selenium import webdriver

# instagram 페이지에서 원하는 해쉬태그로 selenium 접속(+ 크롬 드라이버)
# 상대주소 찾아가기~(첨부파일 한다던가, 데이터베이스 경로 찾는다 한다던가 할 때 사용한다)
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe') # 현재파일에서 뒤로 한번 가서..(그럼 pratice클래스)
                                                                           # 여기에서 /sebdriver클릭- /chromedriver 사용

# .. : 상위로 이동 (그래픽 인터페이스에서 뒤로 가기에 해당하는 것)
# . : 현재
# / : 하위로 이동 (그래픽 인터페이스에서 더블클릭하여 폴더 들어가는 거랑 같은 것)
    # ex) c:/program file/master ...

# https://www.instagram.com/explore/tags/아이즈원/ 가 왜 고양이가 사라졌지?
# URL주소의 한글은 유니코드로 변환(한글이면 깨지는 경우가 있음)
url = 'https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90/'

driver.get(url) # 셀레니움은 자체 프로그램을 통해 긁어오기 때문에 뜨는 속도가 느린 것을 확인 할 수 있다.
#driver.close() # 실행 후 브라우저종료

