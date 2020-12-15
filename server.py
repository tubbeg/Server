from environ import Environment
import signal
import sys


class WSGI_Server():
    def __init__(self):
        pass

    def start_response(self, status, response_headers, exc_info=None):
        raise NotImplementedError()

    def get_environ(self):
        raise NotImplementedError()


class Server(WSGI_Server):
    def __init__(self):
        super().__init__()
        #self.__environment = Environment()
        pass

    def process_request(self, client_connection):
        raise NotImplementedError()

    def make_response(self, app_result):
        raise NotImplementedError()

    def set_application(self, app):
        raise NotImplementedError()

    def serve_forever(self):
        raise NotImplementedError()

    def set_signal_handler(self):
        signal.signal(signal.SIGINT, self.__signal_handler)

    def __signal_handler(self, sig, frame):
        print("SIGINT detected", file=sys.stderr)
        sys.exit(0)
