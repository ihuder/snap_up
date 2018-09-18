# Tornado Handler

import json

import tornado.web
from modle.modle import *


class Basehandler(tornado.web.RequestHandler):
    def get_current_user(self):
        s_cookie = self.get_secure_cookie("user")
        if s_cookie:
            return s_cookie.decode()


class IndexHandler(Basehandler):
    @tornado.web.authenticated
    def get(self):
        return self.render("index.html", user=self.current_user)


class OderHandler(Basehandler):
    @tornado.web.authenticated
    def post(self):
        pass


class UserRegister(Basehandler):
    def post(self, *args, **kwargs):
        user_name = self.get_argument("uname", None)
        password = self.get_argument("upassword", None)
        try:
            User.get(name=user_name)
            return self.render("register.html", errors="user exist")
        except User.DoesNotExist:
            user = User()
            user.new_user(user_name, password)
            self.set_secure_cookie("user", user_name)
            self.render("index.html", user=user_name)

    def get(self):
        self.render("register.html", errors=None)


class UserLogin(Basehandler):
    def post(self, *args, **kwargs):
        user_name = self.get_argument("uname", None)
        password = self.get_argument("upassword", None)
        if user_name and password:
            try:
                user = User.get(name=user_name)
                if user.validate_password(user_name, password):
                    self.set_secure_cookie("user", user_name)
                    self.redirect("/")
                    # self.render("index.html", user=user_name)
                else:
                    self.render("register.html")
            except User.DoesNotExist:
                self.render("register.html")

    def get(self, *args, **kwargs):
        return self.render("login.html")


class UserLogout(Basehandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("user")
        self.redirect("/user/login")


class OrderHandler(Basehandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        amount = Commodity.get(name="phone").amount
        self.finish(amount)

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        user_name = self.get_current_user()
        amount = self.get_argument("amount", None)
        commodity = Commodity.get(name="phone")
