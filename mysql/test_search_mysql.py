import MySQLdb


class MysqlSearch(object):

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='cky1993717',
                db='news',
                port=3306,
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    def get_one(self):
        """准备sql，找到cursor，执行sql，拿到结果，出炉数据，关闭连接"""
        sql = 'SELECT * FROM `news` WHERE `type` = %s ORDER BY `created_at` DESC ;'
        cursor = self.conn.cursor()
        cursor.execute(sql, ('体育', ))
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        cursor.close()
        self.close_conn()
        return rest


    def get_more(self):
        sql = 'SELECT * FROM `news` WHERE `type` = %s ORDER BY `created_at` DESC ;'
        cursor = self.conn.cursor()
        cursor.execute(sql, ('体育',))
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        self.close_conn()
        return rest

    def get_more1(self, page, page_size):
        offset = (page - 1)*page_size
        sql = 'SELECT * FROM `news` WHERE `type` = %s ORDER BY `created_at` DESC LIMIT %s, %s ;'
        cursor = self.conn.cursor()
        cursor.execute(sql, ('体育',offset, page_size))
        rest = [dict(zip([k[0] for k in cursor.description], row)) for row in cursor.fetchall()]
        cursor.close()
        self.close_conn()
        return rest

    def add_one(self):
        try:
            sql = "INSERT INTO `news`(`title`,`image`, `content`, `type`, `is_valid`) VALUE (%s, %s, %s, %s, %s);"
            cursor = self.conn.cursor()
            cursor.execute(sql, ('标题1', '/static/img/news/01.png', '新闻内容1', '推荐', 1))
            self.conn.commit()
            cursor.close()

        except:
            print('error')
            self.conn.rollback()

        self.close_conn()


def main():
    obj = MysqlSearch()
    # rest = obj.get_one()
    # print(rest)
    obj.add_one()

    # rest = obj.get_more()
    # for item in rest:
    #     print(item)
    #     print('-----------')

if __name__ == '__main__':
    main()
