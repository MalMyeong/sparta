from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_music = db.musics.find_one({'title':'사랑의 인사'})
print(target_music)