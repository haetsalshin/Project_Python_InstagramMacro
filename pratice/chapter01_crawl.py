# 지금까지는 한페이지에 모든 것을 만들었다면 지금부터는 java처럼 불러서 하는 걸 만들어 볼거임.

# ** Chapter01_crawl.py
# * requests에서 크롤링하는 부분을 모듈화 하고,
# * import해서 사용하는 용도


# 수집하고 싶은 인스타그램의 #해시태그 페이지 url 주소
from libs.crawler import crawl # libs 패키지의 crawler클래스로부터 crawl()메서드를 호출함.

url = 'https://www.instagram.com/explore/tags/%EA%B3%A0%EC%96%91%EC%9D%B4/' # explore/tags/고양이 /

pageString = crawl(url) # requests를 이제부터 crawl()이 하도록 만들 것임. 이 메서드를 crawler 클래스로 보내서 쓸거임
print(pageString)