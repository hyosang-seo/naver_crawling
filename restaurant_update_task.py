import requests
from bs4 import BeautifulSoup
import csv

url = 'https://search.naver.com/search.naver'


f = open('list.csv','r')
data = f.readlines()

for i in range(0,len(data)):
    params = {
    'query': data[i]
    }

    response = requests.get(url, params=params)
    html = response.text

    # 뷰티풀소프의 인자값 지정
    soup = BeautifulSoup(html, 'html.parser')

    # 쪼개기
    title_list = soup.select('div.txt')

    result = []
    for tag in title_list:
        result +=tag
    print(result)