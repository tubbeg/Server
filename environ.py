

class Environment(object):
    def __init__(self, server_name, request_method, path):
        self.__environ = {}
        self.__environ['wsgi.url_scheme'] = 'http'
        self.__environ['wsgi.input'] =
        self.__environ['wsgi.errors'] =
        self.__environ['wsgi.multithread'] = False
        self.__environ['wsgi.multiprocess'] = False
        self.__environ['wsgi.run_once'] = False
        self.__environ['wsgi.version'] = (1, 0)
        self.__environ['SERVER_NAME'] =
        self.__environ['REQUEST_METHOD'] =
        self.__environ['PATH_INFO'] = path
        self.__environ['SERVER_PORT'] =

    def set_environ(self, environ):
        raise NotImplementedError()

    def get_environ(self):
        return self.__environ