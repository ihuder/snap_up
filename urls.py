from views.views import *

handlers = [
    (r"/", IndexHandler),
    (r"/order", OderHandler),
    (r"/user/login", UserLogin),
    (r"/user/logout", UserLogout),
    (r'/user/register', UserRegister),
    (r'/order', OrderHandler),
]