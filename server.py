import os

from tools.webserver import run


ROOT = os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    print(ROOT)
    run()
