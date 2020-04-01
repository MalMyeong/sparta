from pymongo import MongoClient
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

target_movie = db.movies.find_one({'title':'어벤져스: 엔드게임'})

target_star = target_movie['star']

movies = db.movies.find({'star':target_star})

for movie in movies:
    movies =movie

db.movies.update_many({'star':target_star},{'$set':{'star':'0'}})

