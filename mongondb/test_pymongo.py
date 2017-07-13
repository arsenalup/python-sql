from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId


class Testmongo(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['students']


    def add_one(self):
        """新增数据"""
        post = {
            'title':'新增标题',
            'content':'博客内容',
            'created_at':datetime.now()
        }
        self.db.students.insert_one(post)


    def get_one(self):
        return self.db.students.find_one()

    def get_more(self):
        return self.db.students.find({'age':16})

    def update(self):
        # rest = self.db.students.update_one({'age':16}, {'$inc':{'age':3}} )

        rest = self.db.students.update_many({}, {'$inc':{'age':3}} )
        return rest

    def delete(self):
        # return self.db.students.delete_one({'age':21} )
        return self.db.students.delete_many({'age': 21})


def mian():
    obj = Testmongo()
    # rest = obj.add_one()

    # rest = obj.get_one()
    # print(rest)

    # rest = obj.get_more()
    # for item in rest:
    #     print(item)

    # rest = obj.update()
    # print(rest.matched_count)
    # print(rest.modified_count)


    rest = obj.delete()
    print(rest.deleted_count)

if __name__ == '__main__':
    mian()