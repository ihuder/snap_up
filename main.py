from tornado.options import define
from fire import Fire
import tornado.web
from setting import *
from utils.MyException import *
from urls import handlers
from modle.ModleDecorator import db_models

define("port", default=8080, help="run on the given port", type=int)

settings = dict(
    cookie_secret=SECRET_KEY,
    template_path=TEMPLATE_PATH,
    static_path=STATIC_PATH,
    xsrf_cookies=True,
    debug=DEBUG,
    login_url=LOGIN_URL
)


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, handlers, **settings)


class Server(object):

    def __init__(self):
        pass

    @staticmethod
    def runserver(port=8080):
        tornado.options.parse_command_line()
        app = Application()
        app.listen(port)
        tornado.ioloop.IOLoop.instance().start()

    @staticmethod
    def create_table(table_name=None):
        """
        init database
        :return:
        """
        if DB_TYPE == "sqlite":
            db = SqliteDatabase(DB_PATH)
        elif DB_TYPE == "mysql":
            db = ""
        else:
            raise UnDefineTable
        db.connect()
        if table_name:
            for model in db_models:
                db_obj = getattr(model, table_name)
                if db_obj:
                    db.create_tables([db_obj])
                    return
            else:
                raise UnDefineTable
        else:
            db.create_tables(db_models)

Fire(Server)