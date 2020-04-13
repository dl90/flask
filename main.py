from server.create_server import create_server
from server.config import Config

if __name__ == "__main__":
    create_server(Config).run(port=8888, use_reloader=False)
