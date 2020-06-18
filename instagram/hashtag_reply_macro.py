# * hashtag_reply_macro
# * : 해시태그
# *  선택자를 수시로 변경함

from selenium import webdriver
import time, random
from bs4 import BeautifulSoup


# 1. Chromer Driver Setup
path = '..' # 집이나 다른 곳 가서 사용할 시 경로가 달라 질 수 있기 때문에. 이렇게 따로 객체설정 하면 더 편리하다.
driver = webdriver.Chrome(executable_path='{}/webdriver/chromedriver.exe'.format(path))

# 2. instagram Login
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver.get(url)
time.sleep(3)


# what is xpath?
# : xpath는 W3C의 표준으로 확장 생성하여 문서의 구조를 통해 경로 위에
#   지정한 구문을 사용하여 항목을 배치하고 처리하는 방법을 기술하는 언어
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys("")
 # id 가 react=root를 찾아서 그 아래 section태그로 가라. main->div->article->div->div중 첫번째 div->div->form->2번째 div->label->input
 # 여기서 div[1번부터 시작한다.
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("")
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/botton/div').click()

# 3. HashTag Searching
time.sleep(2)
hash_url = 'https://www.instagram.com/explore/tags/%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90/'
driver.get(hash_url)

# 4. Board List Input & Output
def parse(page_code):
    soup = BeautifulSoup(page_code, 'html.parser')
    feed_list = soup.findAll('div', {'class', 'v1Nh3'}) # hash 값은 수시로 변경됨(실행될 때 마다)
                                                        # 확인해보면 _9AhH0게 전부 리스트로 들어가 있음을 알 수 있다. 이 모든 리스트가 feed_list에 담김
    print('Feed Cnt:', len(feed_list))


    links = []
    for one in feed_list:
        print(one)
        insta_link = 'http://www.instagram.com/'
        link_addr = one.find('a')['href']
        print(insta_link + link_addr)
        links.append(insta_link+ link_addr)

    return links


time.sleep(4)
page_code = driver.page_source
links = parse(page_code)
print('Feed Cnt:', len(links))

# 좋아요 누르고 댓글 달기
for url in links:
    try:
        driver.get(url)

        rnd_sec = random.randint(5, 15)
        time.sleep(rnd_sec)
        message = '대박! 아이즈원:)'

        # 좋아요
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()

        #댓글
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys(message)
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
    except Exception as e:
        print(e)