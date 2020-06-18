import requests

def crawl(url):
    resp = requests.get(url) # url 소스코드를 resp에 할당하고
    print(resp, url) #출력하는 것
    return resp.content # 나를 호출한 곳에 다시 이 값을 전달하시오 ~> chapter01에서 호출했기 때문에 소스코드 값들이 간다.