# 데이터를 받아 json 파일에 저장하는 코드
import requests
import json
from pprint import pprint

total_data = []

def movie_info(genres):
    # 1페이지부터 500페이지까지의 데이터를 가져옴.
    for i in range(1, 100):
        BASE_URL = "https://api.themoviedb.org/3"
        path = '/movie/popular'
        params = {
            'api_key': '86bdc6ba5098674a46de6901a230c5f7',
            'page': i
        }
        movies = requests.get(BASE_URL+path, params=params).json().get('results')

        for movie in movies:
            if movie.get('release_date', ''):
                # Movie 모델 필드명에 맞추어 데이터를 저장함.
                fields = {
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'grade': movie['vote_average'],
                    'description': movie['overview'],
                    'poster_path': movie['poster_path'],
                    # 'bookmark': False,
                    'genre_ids': movie['genre_ids']
                }
                data = {
                    'pk': movie['id'],
                    'model': 'movies.movie',
                    'fields': fields,
                }

                genre_names = []
                for i in range(len(genres)):
                    if genres[i]['id'] in fields.get('genre_ids'):
                        genre_names.append(genres[i]['name'])
                fields['genres'] = genre_names
                del fields['genre_ids']
                total_data.append(data)
    # print(len(total_data))
    # pprint(total_data)
    return total_data

genre_json = open('./genres.json', encoding='UTF-8')
genre_dict = json.load(genre_json)
movie_info(genre_dict)
with open('movies.json', 'w', encoding='UTF-8') as f:
    json.dump(total_data, f, indent='\t')