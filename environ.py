import sys


class Environment(object):
    def __init__(self, server_name, request_method, path, stream, port):
        self.__environ = {}
        self.__environ['wsgi.url_scheme'] = 'http'
        self.__environ['wsgi.input'] = stream
        self.__environ['wsgi.errors'] = sys.stderr
        self.__environ['wsgi.multithread'] = False
        self.__environ['wsgi.multiprocess'] = False
        self.__environ['wsgi.run_once'] = False
        self.__environ['wsgi.version'] = (1, 0)
        self.__environ['SERVER_NAME'] = server_name
        self.__environ['REQUEST_METHOD'] = request_method
        self.__environ['PATH_INFO'] = path
        self.__environ['SERVER_PORT'] = port

    def set_environ(self, environ):
        self.__environ = environ

    def set_variables(self, server_name, request_method, path, stream, port):
        self.__environ['SERVER_NAME'] = server_name
        self.__environ['REQUEST_METHOD'] = request_method
        self.__environ['PATH_INFO'] = path
        self.__environ['SERVER_PORT'] = port
        self.__environ['wsgi.input'] = stream

    def get_environ(self):
        return self.__environ
