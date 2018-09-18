import datetime
from hashlib import md5
from modle.ModleDecorator import register_db

from peewee import Model, CharField, DateTimeField, IntegerField, BooleanField

from setting import *


class BaseModel(Model):
    class Meta:
        database = DB


@register_db
class Orders(BaseModel):
    id = IntegerField(primary_key=True)
    item_id = IntegerField()
    user_id = IntegerField()
    amount = IntegerField(default=0)
    status = BooleanField(default=False)
    c_time = DateTimeField(default=datetime.datetime.now)
    f_time = DateTimeField()


@register_db
class User(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True)
    password_s3 = CharField()

    class Meta:
        database = DB

    def gen_password(self, user_name, password):
        mas = md5()
        mas.update("".join([user_name, password, SECRET_KEY]).encode())
        self.password_s3 = mas.digest().hex()
        return self.password_s3

    def validate_password(self, user_name, password):
        mas = md5()
        mas.update("".join([user_name, password, SECRET_KEY]).encode())
        _password = mas.digest().hex()
        if _password == self.password_s3:
            return True
        else:
            return False

    def new_user(self, user_name, password):
        password = self.gen_password(user_name, password)
        self.name = user_name
        self.password_s3 = password
        self.save()


@register_db
class Commodity(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    amounts = IntegerField()


@DB.atomic()
def snap_up(user, amount):
    """
    抢购事务
    :return:
    """
    order = Orders()
    order.item_id = 1
    order.user_id = user.id
    order.amount = 1
    order.f_time = datetime.datetime.now


