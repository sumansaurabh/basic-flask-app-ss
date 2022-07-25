import asyncio
from turtle import st
import tornado.httpserver
import tornado.options
import tornado.web
import sys
from tornado.options import define, options
# generate random floating point values
from random import seed
from random import random
seed(1)

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world. From port - "+str(options.port))

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        print("hello ::: ",self.request.files)
        file1 = self.request.files['file'][0]
        original_fname = file1['filename']

        output_file = open("uploads/" + original_fname, 'wb')
        output_file.write(file1['body'])

        self.finish("file " + original_fname + " is uploaded")

    def get(self):

        arr = [1] * 1024*30
        for i in range(len(arr)):
            arr[i] = random()
        arr = str(arr)
        print("size of arr:  ",sys.getsizeof(arr))
        self.finish("heello" + arr)

async def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([(r"/", MainHandler), (r"/upload", UploadHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    print("Server running -- ", options.port)
    http_server.listen(options.port)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())