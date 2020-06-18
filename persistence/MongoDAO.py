from pymongo import MongoClient


# 클래스는 뭐다? 설계도. 때문에 혼자서는 아무것도 못함. 객체를 생성해야 쓸 수 있다.

# mDao = MongoDAO() # 객체 생성
# mDao < 객체를 통해 만들어진 결과

# Connection 단계가 필요함.

# mDao.mongo_write()
# mDao.mongo_select_all()

class MongoDAO:
    reply_list = [] # mongoDB Document를 담을 list 선언

    def __init__(self): # 생성자
        # >> mongoDB Connection
        # 객체를 생성할 때 하는 flow
        self.client = MongoClient('127.0.0.1', 27017) # 클래스 객체 할당(ip, Port)
        self.db = self.client['local'] # MongoDB의 'local' DB를 할당. mongoDB compass 에 있는 local에 전달하겠다는 뜻
        self.collection = self.db.get_collection('movie') # 동적으로 Collection 선택. local에 들어가서 그 안에 있는 movie에
                                                          # 전달을 하겠다는 뜻

    # MongoDN에 input
    def mongo_wirte(self, data):
        print('>> mongoDB WRITE DATA:')
        self.collection.insert(data) # JSON Type = Dict Type(Python)

    # MongoDB에서 SelectAll
    def mongo_select_all(self):
        for one in self.collection.find({}, {'_id':0, 'content':1, 'score':1}):
            self.reply_list.append([one['title'], one['content'], one['score']]) # dict에서 value와 score만 추출
        return self.reply_list







