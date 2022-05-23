# import requests
# import json

# TMDB_API_KEY = '58c1093eb07e01e119c6d992fa591aa6'

# request_url = "https://api.themoviedb.org/3/genre/movie/list"
# params = {
#     'api_key': '86bdc6ba5098674a46de6901a230c5f7'
# }
# results = requests.get(request_url, params=params).json()

# total_data = []

# for genre in results['genres']:
#     fields = {
#         'id': genre['id'],
#         'name': genre['name']
#     }

#     total_data.append(fields)

# with open('genres.json', 'w', encoding='utf-8') as f:
#     json.dump(total_data, f, indent='\\t')