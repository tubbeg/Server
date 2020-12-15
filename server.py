from environ import Environment


class WSGI_Server():
    def __init__(self):
        raise NotImplementedError()

    def start_response(self, status, response_headers, exc_info=None):
        raise NotImplementedError()

    def get_environ(self):
        raise NotImplementedError()


class Server(WSGI_Server):
    def __init__(self):
        super().__init__()
        self.__environment = Environment()
        raise NotImplementedError()

    def process_request(self, client_connection):
        raise NotImplementedError()

    def make_response(self, app_result):
        raise NotImplementedError()

    def set_application(self, app):
        raise NotImplementedError()

    def serve_forever(self):
        raise NotImplementedError()
