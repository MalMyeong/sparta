from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # client에서 'dbsparta'라는 이름의 db를 만듭니다.
# dbsparta라는 이름의 db를 만들어 그 db에 대한 연결을 db라는 변
# mongoDB에 insert하기

# 'users'라는 collection을 만들고 거기에 한개의 문서를 넣는다 -> {'name':'bobby','age':21}를 넣습니다.
#db.users.insert_one({'name':'bobby','age':21}) # 컬렉션이 생성, insert_one는 한개씩 넣는다는 의미
#db.users.insert_one({'name':'kay','age':27})
#db.users.insert_one({'name':'john','age':30})

#all_users = list(db.users.find()) # db.users로 받아서 리스트로 만든다(?)
#same_ages = list(db.users.find({'age':21})) # 특정 조건의 데이터 보기

#특정 결과값 뽑기
#users = db.users.find_one({'name':'bobby'}) # 괄호 안 조건과 일치하는 문서를 한개만 찾아서 돌려준다

#users = db.users.find_one({'name':'bobby'},{'_id':0}) # _id 에서 언더바의 의미는 언더바 친 정보는 제외하고 불러오는 것


#수정하기
db.users.update_one({'name':'bobby'},{'$set':{'age':19}}) #update_one 하나만 바꿔주고, update는 다 바꿔준다

user = db.users.find_one({'name':'bobby'})
print (user)