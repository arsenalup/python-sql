import redis


class Base(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

class TestString(object):

    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_set(self):
        rset = self.r.set('user2', 'amy')
        print(rset)
        return rset

    def get_tset(self):
        rset = self.r.get('user2')
        print(rset)
        return rset

    def test_mset(self):
        d = {
            'user3': 'tom',
            'user4': 'orl'
        }
        rset = self.r.mset(d)
        print(rset)
        return rset

    def get_mtest(self):
        l = ['user3', 'user4']
        rset = self.r.mget(l)
        print(rset)
        return rset

    def test_del(self):
        rset = self.r.delete('user3')
        print(rset)
        return rset


class TestList(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def test_push(self):
        t = ('amy', 'jhon')
        rset = self.r.lpush('eat1', *t)
        print(rset)
        rset = self.r.lrange('eat1', 0, -1)
        print(rset)

    def test_pop(self):
        rset = self.r.lpop('eat1')
        print(rset)


class TestSet(Base):

    def test_add(self):
        l = ['cat', 'dog']
        rset = self.r.sadd('zoon2', *l)
        print(rset)
        rset = self.r.smembers('zoon2')
        print(rset)

    def test_srem(self):
        rset = self.r.srem('zoon2', 'dog')
        print(rset)
        rset = self.r.smembers('zoon2')
        print(rset)


class Test_Hash(Base):
    def test_set(self):
        rset = self.r.hset('stu:xxx', 'name', 'amy')
        print(rset)
        rset = self.r.hexists('stu:xxx', 'name')
        print(rset)




def main():
    # str_obj = TestString()
    # str_obj.test_set()

    # str_obj.get_tset()
    # str_obj.test_mset()
    # str_obj.get_mtest()
    # str_obj.test_del()


    # str_obj = TestList()
    # str_obj.test_push()
    # str_obj.test_pop()

    # str_obj = TestSet()
    # str_obj.test_add()

    str_obj = Test_Hash()
    str_obj.test_set()
if __name__ == '__main__':
    main()
