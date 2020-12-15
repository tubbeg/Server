from server import Server
import time

def make_server():
    server = Server()
    server.set_signal_handler()
    for _ in range(0, 100):
        print(10)
        time.sleep(10)
    raise NotImplementedError()


if __name__ == '__main__':
    make_server()