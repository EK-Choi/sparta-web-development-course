from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# (1) 영화제목 '매트릭스'의 평점을 가져오기
target_movie = db.movies.find_one({'title':'매트릭스'})
print(target_movie['rate'])

# (2) '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기
target_rate = target_movie['rate']
movies = list(db.movies.find({'rate':target_rate}))

for movie in movies:
    print(movie['title'])

# (3) 매트릭스 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'rate':'0'}})