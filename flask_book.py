from __future__ import absolute_import

from flask import _request_ctx_stack

class Facebook(object):

    def __init__(self, app):
        self.app = app
        self.app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        self.app.teardown_request(self.teardown_request)
        self.app.before_request(self.before_request)

    def connect(self):
        return sqlite3.connect(self.app.config['SQLITE3_DATABASE'])

    def before_request(self):
        ctx = _request_ctx_stack.top
        ctx.sqlite3_db = self.connect()

    def teardown_request(self, exception):
        ctx = _request_ctx_stack.top
        ctx.sqlite3_db.close()

    def get_db(self):
        ctx = _request_ctx_stack.top
        if ctx is not None:
            return ctx.sqlite3_db
