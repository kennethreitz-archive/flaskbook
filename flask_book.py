from __future__ import absolute_import

from flask import _request_ctx_stack


class Facebook(object):

    def __init__(self, app):
        self.app = app
        self.app.config.setdefault('FACEBOOK_APP_ID', None)
        self.app.config.setdefault('FACEBOOK_SECRET', None)



    # def before_request(self):
    #     ctx = _request_ctx_stack.top
    #     ctx.sqlite3_db = self.connect()

    # def teardown_request(self, exception):
    #     ctx = _request_ctx_stack.top
    #     ctx.sqlite3_db.close()

    # def get_db(self):
    #     ctx = _request_ctx_stack.top
    #     if ctx is not None:
    #         return ctx.sqlite3_db


