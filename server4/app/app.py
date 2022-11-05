from base64 import decode
from flask import Flask, request


app = Flask(__name__)
PORT = 5004
HOST = 'localhost'


def reverseS(inS):
    reverse = str(inS)[::-1]
    return int(reverse)


@app.route('/')
def server2():
    inS = int(request.data)
    ret = reverseS(inS)
    print(ret)
    print(f'server4_1 | Server four reversed {inS} into {str(ret)}')
    return str(ret)


if __name__ == '__main__':
    print("Starting new_hw6_server1_1 ... done")
    app.run(host=HOST, port=PORT)
