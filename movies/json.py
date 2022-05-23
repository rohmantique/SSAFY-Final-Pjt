
# import requests
# import json

# def get_movie_datas():
#     total_data = []

#     for i in range(1, 501):
#         request_url = f"<https://api.themoviedb.org/3/movie/now_playing?api_key={'86bdc6ba5098674a46de6901a230c5f7'}&language=ko-KR&page={i}>"
#         movies = requests.get(request_url).json()

#         for movie in movies['results']:
#             data = {
#                 'title': movie['title'],
#                 'release_date': movie['release_date'],
#                 'grade': movie['vote_averate'],
#                 'description': movie['overview'],
#                 'genres': movie['genres'],
#             }
#         total_data.append(data)
    
#     json_data = {
#         'name': 'movie data',
#         'data': data,
#     }
#     with open('movie_data.json', 'w', encoding='utf-8') as w:
#         json.dump(json_data, w, indent='\\t', ensure_ascii=False)

# get_movie_datas()