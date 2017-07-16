import redis


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
            'user3':'tom',
            'user4':'orl'
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




def main():
    str_obj = TestString()
    # str_obj.test_set()

    # str_obj.get_tset()
    # str_obj.test_mset()
    # str_obj.get_mtest()
    str_obj.test_del()
if __name__ == '__main__':
    main()
