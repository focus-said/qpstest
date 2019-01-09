#! /usr/bin/env python 
# -*- coding: utf-8 -*-
# @author: focus
# @Time : 2019/1/9 5:27 PM
# @Software: PyCharm
import time
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado import gen
from tornado.options import define, options

define("port", default=8899, help="run on the given port", type=int)


class Manager(tornado.web.RequestHandler):
    #  主处理函数
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, data):
        # reqs = self.request.body_arguments
        # yield gen.sleep(0.001)
        self.write(str(True))
        self.finish()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/(\w+)', Manager), ], )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

