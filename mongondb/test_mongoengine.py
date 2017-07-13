from mongoengine import connect, Document, StringField, IntField, FloatField, EmbeddedDocument, ListField, EmbeddedDocumentField

connect('students')

SEX_CHOICES = (
    ('male', '男'),
    ('famale', '女'),
)

class Grade(EmbeddedDocument):
    name = StringField(required=True)
    score = FloatField(required=True)


class students(Document):
    name = StringField(max_length=32, required=True)
    age = IntField( required=True)
    sex = StringField(choices=SEX_CHOICES, required=True)
    grade= ListField(EmbeddedDocumentField(Grade))

    meta = {
        'collection': 'students'
    }

class TestMongoEngine(object):

    def add_one(self):
        ''' 新增数据 '''
        yuwen = Grade(
            name='语文',
            score=95
            )
        english = Grade(
            name='英语',
            score=89)
        stu_obj = students(
            name='张三',
            age=21,
            sex='male',
            grade=[yuwen, english]
        )
        # stu_obj.test = 'OK'
        stu_obj.save()
        return stu_obj

    def get_one(sele):
        return students.objects.first()

    def get_more(self):
        ''' 查询多条数据 '''
        # return Student.objects
        return Student.objects.all()

    def get_one_from_oid(self, oid):
        ''' 查询指定ID的数据 '''
        return Student.objects.filter(id=oid).first()

    def update(self):
        ''' 修改数据 '''
        # 修改一条数据
        # rest = Student.objects.filter(sex='male').update_one(inc__age=1)
        # return rest
        # 修改多条数据
        rest = Student.objects.filter(sex='male').update(inc__age=1)
        return rest

    def delete(self):
        ''' 删除数据 '''
        # 删除一条数据
        rest = Student.objects.filter(sex='male').first().delete()
        # 删除多条数据
        rest = Student.objects.filter(sex='male').delete()
        return rest


def main():
    obj = TestMongoEngine()
    # rest = obj.add_one()
    # print(rest.id)

    rest = obj.get_one()
    print(rest.id)

    # rest = obj.get_more()
    # print(type(rest))
    # for item in rest:
    #     print(item.id)

    # rest = obj.get_one_from_oid('593bb8e7fa3ebd091078d40e')
    # print(rest.name)

    # rest = obj.update()
    # print(rest)

    # rest = obj.delete()
    # print(rest)

if __name__ == '__main__':
    main()