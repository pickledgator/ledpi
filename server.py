#!/usr/bin/env python

import logging
import os
import tornado.web

logging.basicConfig(
            format="[%(asctime)s][%(name)s](%(levelname)s) %(message)s", level=logging.DEBUG)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class RequestHandler(tornado.web.RequestHandler):
    def initialize(self, logger):
        self.logger = logger

    def post(self):
        print(self)
        self.write("Done")

def main():
    port = 8080
    logger  = logging.getLogger("Server")
    handlers = [
        (r"/", IndexHandler, dict()),
        (r"/geocode", RequestHandler, dict(logger=logger))
    ]
    settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static")                                                                                                 )
    logger.info("Server listening on port {}".format(port))
    app = tornado.web.Application(handlers, **settings)
    app.listen(port)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()


if __name__ == "__main__":
    main()
