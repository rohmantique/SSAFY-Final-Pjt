import requests
import csv
from bs4 import BeautifulSoup
import random

reviews_required = 10000
reviews = []
review_data = []


for page in range(1, 2000):
    NAVER_URL = f'https://movie.naver.com/movie/point/af/list.naver?&page={page}'
    response = requests.get(NAVER_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    reviews = soup.find_all('td', {"class": "title"})

    # 한 페이지의 10개 리뷰 리스트에서 리뷰 한개씩 추출
    for review in reviews:
        content = review.find('a', {'class':'report'}).get('onclick').split("',")[2][2:]
        # 별점만 준 리뷰는 제외
        if content != '':
            movie = review.find('a', {'class':'movie color_b'}).get_text()
            score = review.find('em').get_text()

            user = f'user_{random.randrange(1000, 9999, 1)}'
            review_data.append([movie, user, content, int(score)])
            reviews_required -= 1
    
    # 현재까지 수집된 리뷰가 목표 data sample을 채웠다면 크롤링 중지
    if reviews_required == 0:
        break

columns = ['title', 'user', 'sentence', 'score']

with open('naver_review.csv', 'w', newline='', encoding='UTF-8') as f:
    write = csv.writer(f)
    write.writerow(columns)
    write.writerows(review_data)


# titles = []
# MOVIES_URL = 'https://movie.naver.com/movie/point/af/list.naver?&page=1'
# response = requests.get(MOVIES_URL)
# soup = BeautifulSoup(response.content, 'html.parser')
# movies = soup.find_all('option')
# for movie in movies:
#     titles.append(movie.get_text())

# titles = titles[1:-2]
# column = ['title']

# with open('current_movies.csv', 'w', newline='', encoding='UTF-8') as m:
#     write = csv.writer(m)
#     write.writerow(column)
#     for title in titles:
#         write.writerow([title])